from django.core.management.base import BaseCommand
from django.core.files import File
from portfolio.models import AboutMe, CompanyLogo, BombayShark, GalleryImage
import os
from pathlib import Path


class Command(BaseCommand):
    help = 'Upload images from Personal Photos and Logos folders to database'
    
    def handle(self, *args, **kwargs):
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        
        # Upload profile photo
        self.upload_profile_photo(base_dir)
        
        # Upload company logos
        self.upload_company_logos(base_dir)
        
        # Upload Bombay Sharks hero image
        self.upload_bombay_sharks_images(base_dir)
        
        self.stdout.write(self.style.SUCCESS('\n✓ All images uploaded successfully!'))
    
    def upload_profile_photo(self, base_dir):
        """Upload profile photo to About Me"""
        photos_dir = base_dir / "Personal Photos"
        
        # Use the original photo as specified by user
        profile_photo_path = photos_dir / "Mumbai City Fc solo photo original.jpg"
        
        if profile_photo_path.exists():
            about_me = AboutMe.objects.first()
            if about_me:
                with open(profile_photo_path, 'rb') as f:
                    about_me.profile_photo.save(
                        profile_photo_path.name,
                        File(f),
                        save=True
                    )
                self.stdout.write(self.style.SUCCESS(f'✓ Uploaded profile photo: {profile_photo_path.name}'))
            else:
                self.stdout.write(self.style.WARNING('⚠ About Me entry not found'))
        else:
            self.stdout.write(self.style.WARNING(f'⚠ Profile photo not found: {profile_photo_path}'))
    
    def upload_company_logos(self, base_dir):
        """Upload company logos"""
        logos_dir = base_dir / "Logos"
        
        # Mapping of company names to logo files
        logo_mapping = {
            "Bombay Sharks": "Bombay Sharks.jpg",
            "Hyperlink": "Hyperlink logo.png",
            "India Khelo Football": "India Khelo Football Logo.png",
            "Jaipur Pink Panthers": "Jaipur Pink Panthers Logo.png",
            "Mumbai City FC": "Mumbai City FC Logo.jpg",
            "Mumbai Cricket Association": "Mumbai Cricket Association Logo.png",
            "Pro Govinda": "Pro Govinda Logo.jpg",
            "Rajasthan Royals": "Rajasthan Royals logo.jpg",
            "Reckoning eSports": "Reckoning eSports logo.jpg",
            "SportVot": "SportVot logo.png",
            "SportsTiger": "SportsTiger logo.jpg",
            "Ultimate Table Tennis": "Ultimate Table Tennis Logo.jpg",
            "Para Football": "para football logo.png",
        }
        
        for company_name, logo_filename in logo_mapping.items():
            logo_path = logos_dir / logo_filename
            
            if logo_path.exists():
                try:
                    company = CompanyLogo.objects.get(company_name=company_name)
                    with open(logo_path, 'rb') as f:
                        company.logo.save(
                            logo_filename,
                            File(f),
                            save=True
                        )
                    self.stdout.write(self.style.SUCCESS(f'✓ Uploaded logo for {company_name}'))
                except CompanyLogo.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'⚠ Company not found: {company_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠ Logo not found: {logo_path}'))
    
    def upload_bombay_sharks_images(self, base_dir):
        """Upload Bombay Sharks hero image and gallery"""
        photos_dir = base_dir / "Personal Photos"
        
        sharks = BombayShark.objects.first()
        if not sharks:
            self.stdout.write(self.style.WARNING('⚠ Bombay Sharks Academy entry not found'))
            return
        
        # Use a suitable photo for the hero image
        # Since we don't have a specific Bombay Sharks photo, we'll use a football-related one
        hero_candidates = [
            "Mumbai City FC team photo.jpg",
            "Mumbai City Fc old photo with trophy.jpg",
        ]
        
        for candidate in hero_candidates:
            hero_path = photos_dir / candidate
            if hero_path.exists() and not sharks.hero_image:
                with open(hero_path, 'rb') as f:
                    sharks.hero_image.save(
                        candidate,
                        File(f),
                        save=True
                    )
                self.stdout.write(self.style.SUCCESS(f'✓ Uploaded Bombay Sharks hero image: {candidate}'))
                break
        
        # Add remaining photos to gallery
        gallery_photos = [
            "Jaipur Pink Panthers solo photo 1.jpg",
            "Jaipur Pink Panthers solo photo 2.jpg",
            "Mumbai city fc solo photo.jpg",
        ]
        
        for photo_name in gallery_photos:
            photo_path = photos_dir / photo_name
            if photo_path.exists():
                # Check if already exists
                if not GalleryImage.objects.filter(academy=sharks, caption=photo_name).exists():
                    gallery_img = GalleryImage(academy=sharks, caption=photo_name.replace('.jpg', ''))
                    with open(photo_path, 'rb') as f:
                        gallery_img.image.save(
                            photo_name,
                            File(f),
                            save=True
                        )
                    self.stdout.write(self.style.SUCCESS(f'✓ Added gallery image: {photo_name}'))
