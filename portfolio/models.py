from django.db import models
from django.core.validators import EmailValidator, URLValidator
from ckeditor.fields import RichTextField


class AboutMe(models.Model):
    """
    Singleton model for About Me section - only one instance should exist
    """
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, help_text="Professional title/role")
    bio = RichTextField(help_text="Professional summary and background")
    profile_photo = models.ImageField(upload_to='profile/', help_text="Your professional photo")
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=20, blank=True)
    
    # Social media links
    linkedin_url = models.URLField(blank=True, validators=[URLValidator()])
    instagram_url = models.URLField(blank=True, validators=[URLValidator()])
    twitter_url = models.URLField(blank=True, validators=[URLValidator()])
    
    # Resume
    resume = models.FileField(upload_to='resume/', blank=True, help_text="Upload CV/Resume PDF")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists (singleton pattern)
        if not self.pk and AboutMe.objects.exists():
            raise ValueError("Only one About Me instance can exist")
        return super().save(*args, **kwargs)


class Experience(models.Model):
    """
    Work experience entries
    """
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if current position")
    description = RichTextField(help_text="Job responsibilities and achievements")
    company_logo = models.ImageField(upload_to='experiences/', blank=True)
    is_current = models.BooleanField(default=False, help_text="Currently working here")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
    
    def __str__(self):
        return f"{self.role} at {self.company}"


class BombayShark(models.Model):
    """
    Bombay Sharks Football Academy section - singleton model
    """
    title = models.CharField(max_length=200, default="Bombay Sharks Football Academy")
    subtitle = models.CharField(max_length=300, default="Founder | May 2025 - Present")
    hero_image = models.ImageField(upload_to='bombay_sharks/', help_text="Main academy photo")
    description = RichTextField(help_text="Academy details and philosophy")
    
    # Academy details
    age_groups = models.CharField(max_length=100, default="U-6 to U-15")
    locations = models.TextField(help_text="Operating locations across Mumbai")
    training_philosophy = RichTextField(help_text="Training approach and methodology")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Bombay Sharks Academy"
        verbose_name_plural = "Bombay Sharks Academy"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.pk and BombayShark.objects.exists():
            raise ValueError("Only one Bombay Sharks instance can exist")
        return super().save(*args, **kwargs)


class GalleryImage(models.Model):
    """
    Gallery images for Bombay Sharks section
    """
    academy = models.ForeignKey(BombayShark, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='bombay_sharks/gallery/')
    caption = models.CharField(max_length=300, blank=True)
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
    
    def __str__(self):
        return f"Gallery Image {self.id}"


class Certification(models.Model):
    """
    Professional certifications and courses
    """
    name = models.CharField(max_length=300, help_text="Certification name")
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True)
    certificate_image = models.ImageField(upload_to='certifications/', blank=True, 
                                         help_text="Certificate badge or image")
    order = models.IntegerField(default=0, help_text="Display order")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-issue_date', 'order']
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
    
    def __str__(self):
        return self.name


class ContactSubmission(models.Model):
    """
    Contact form and enrollment submissions
    """
    ENROLLMENT_INTERESTS = [
        ('general', 'General Inquiry'),
        ('academy', 'Academy Enrollment'),
        ('both', 'Both'),
    ]
    
    AGE_GROUPS = [
        ('U6', 'Under 6'),
        ('U8', 'Under 8'),
        ('U10', 'Under 10'),
        ('U12', 'Under 12'),
        ('U15', 'Under 15'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    # Enrollment specific fields
    interest_type = models.CharField(max_length=20, choices=ENROLLMENT_INTERESTS, default='general')
    age_group = models.CharField(max_length=10, choices=AGE_GROUPS, blank=True)
    
    # Admin fields
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.submitted_at.strftime('%Y-%m-%d')})"


class CompanyLogo(models.Model):
    """
    Companies/brands worked with - for logo showcase
    """
    company_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='company_logos/')
    website_url = models.URLField(blank=True, validators=[URLValidator()])
    display_on_homepage = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'company_name']
        verbose_name = "Company Logo"
        verbose_name_plural = "Company Logos"
    
    def __str__(self):
        return self.company_name
