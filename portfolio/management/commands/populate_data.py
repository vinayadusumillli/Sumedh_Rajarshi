from django.core.management.base import BaseCommand
from portfolio.models import (
    AboutMe, Experience, BombayShark, Certification, CompanyLogo
)
from datetime import date
import os
from django.core.files import File


class Command(BaseCommand):
    help = 'Populate initial portfolio data for Sumedh Rajarshi'
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Populating portfolio data...')
        
        # Create About Me (if doesn't exist)
        if not AboutMe.objects.exists():
            about_me = AboutMe.objects.create(
                name="Sumedh Rajarshi",
                title="Football Operations & Player Welfare Professional",
                bio="""<p>A football operations and player welfare professional with experience across elite club environments, domestic leagues, youth scouting frameworks and grassroots development.</p>
                <p>Skilled in player support systems, team logistics, matchday delivery, safeguarding protocols and talent identification. Built a foundation across football structures ranging from professional men's teams to early-stage youth development pathways, combining operational efficiency with child-centred training understanding.</p>
                <p>Founder of Bombay Sharks Football Academy, a growing grassroots football space for early-age learning across Mumbai.</p>""",
                email="contact@sumedhrajarshi.com",
                phone="+91",
            )
            self.stdout.write(self.style.SUCCESS('Created About Me'))
        
        # Create Bombay Sharks Academy
        if not BombayShark.objects.exists():
            sharks = BombayShark.objects.create(
                title="Bombay Sharks Football Academy",
                subtitle="Founder | May 2025 - Present",
                description="""<p>A developing grassroots football academy for U-6 to U-15, operating across Mumbai (budding phase).</p>
                <p>Centre structure built on age-appropriate technical development, game understanding and motor skill foundations.</p>
                <p>Training model aligned with AIFF Grassroots and FIFA child-centred coaching principles.</p>
                <p>Sessions designed to encourage early football literacy, participation confidence and value-based sporting behaviour.</p>
                <p>Friendly fixtures, festival days and basic competitive exposure introduced to support progressive growth.</p>""",
                age_groups="U-6 to U-15",
                locations="Operating across Mumbai",
                training_philosophy="""<p>Our training approach is built on AIFF Grassroots and FIFA child-centred coaching principles, focusing on age-appropriate technical development, game understanding, and motor skill foundations.</p>
                <p>We emphasize early football literacy, participation confidence, and value-based sporting behaviour to create well-rounded young athletes.</p>"""
            )
            self.stdout.write(self.style.SUCCESS('Created Bombay Sharks Academy'))
        
        # Create Experiences
        experiences_data = [
            {
                "company": "India Khelo Football (IKF)",
                "role": "Video Scout",
                "start_date": date(2025, 10, 1),
                "is_current": True,
                "description": """<ul>
                    <li>Scouting young talent nationwide through video analysis</li>
                    <li>Subroto Cup scouting contributions under structured youth benchmarks</li>
                    <li>Reviewed talent with guidance from Premier League academy scouts</li>
                    <li>Created consolidated scouting clips and development evaluation notes</li>
                </ul>"""
            },
            {
                "company": "Mumbai City FC",
                "role": "Player Welfare Executive",
                "start_date": date(2024, 7, 1),
                "is_current": True,
                "description": """<ul>
                    <li>Liaison for all foreign and domestic players for onboarding and daily support</li>
                    <li>Visa documentation and processing for international players and coaches</li>
                    <li>Flight ticketing and full accommodation setup for away fixtures</li>
                    <li>SIM, banking, PAN and residence assistance during arrival and transfers</li>
                    <li>Matchday and training logistics support including access, transport and setup</li>
                    <li>Cultural orientation and city movement guidance</li>
                    <li>Ongoing welfare reporting to Director of Football and Team Operations</li>
                </ul>"""
            },
            {
                "company": "Jaipur Pink Panthers",
                "role": "Team Manager",
                "start_date": date(2023, 10, 1),
                "end_date": date(2024, 2, 28),
                "description": """<ul>
                    <li>Directed team logistics, travel bookings and training facility alignment</li>
                    <li>Managed full equipment cycle from procurement to upkeep</li>
                    <li>Matchday operations including security, hospitality and access coordination</li>
                    <li>Vendor negotiation and operational budgeting</li>
                    <li>Liaison function across players, support staff and technical management</li>
                </ul>"""
            },
            {
                "company": "Hyperlink Brand Solutions",
                "role": "Event Production Coordinator",
                "start_date": date(2023, 9, 1),
                "end_date": date(2023, 9, 30),
                "description": """<ul>
                    <li>On-ground execution of client expectations and event layouts</li>
                    <li>Vendor coordination, staging prep and show-day compliance checks</li>
                    <li>Final inspection of installations and guest service structures</li>
                </ul>"""
            },
            {
                "company": "Ultimate Table Tennis",
                "role": "Venue Operations",
                "start_date": date(2023, 7, 1),
                "end_date": date(2023, 7, 31),
                "description": """<ul>
                    <li>Allocated venue power needs via generator mapping</li>
                    <li>Setup of Wi-Fi, CCTV network, barricading and fire compliance</li>
                    <li>Managed lighting deployment, room readiness and security teams</li>
                </ul>"""
            },
        ]
        
        for exp_data in experiences_data:
            if not Experience.objects.filter(company=exp_data['company'], role=exp_data['role']).exists():
                Experience.objects.create(**exp_data)
                self.stdout.write(self.style.SUCCESS(f'Created experience: {exp_data["role"]} at {exp_data["company"]}'))
        
        # Create Certifications (sample - you can add all 24+)
        certifications_data = [
            {"name": "AIFF Blue Cubs Leaders Course Level 1", "org": "All India Football Federation", "date": date(2025, 6, 1)},
            {"name": "Association Training: International & Domestic Transfers", "org": "FIFA", "date": date(2025, 6, 1)},
            {"name": "Level 1: Performance Analysis in Football", "org": "PFSA", "date": date(2025, 6, 1)},
            {"name": "Level 1: Technical Scouting in Football", "org": "PFSA", "date": date(2025, 6, 1)},
            {"name": "Level 1: Data Analysis in Football", "org": "PFSA", "date": date(2025, 5, 1)},
            {"name": "Level 1: Opposition Analysis in Football", "org": "PFSA", "date": date(2025, 5, 1)},
            {"name": "Level 1: Talent Identification in Football", "org": "PFSA", "date": date(2025, 5, 1)},
            {"name": "AIFF D Licence", "org": "All India Football Federation", "date": date(2025, 4, 1)},
            {"name": "FIFA Grassroots Children's Soccer Coach", "org": "Escuela de Entrenadores", "date": date(2025, 4, 1)},
            {"name": "EE Playmaker", "org": "The FA", "date": date(2025, 3, 1)},
            {"name": "Introduction Into Football Scouting", "org": "PFSA", "date": date(2025, 3, 1)},
            {"name": "Introduction to Talent Identification in Football", "org": "The FA", "date": date(2024, 9, 1)},
            {"name": "FIFA Guardians™ Developing Your Safeguarding Effectiveness", "org": "FIFA", "date": date(2024, 7, 1)},
            {"name": "FIFA Guardians™ Safeguarding Essentials", "org": "FIFA", "date": date(2024, 7, 1)},
            {"name": "FIFA Guardians™ Starting Your Safeguarding Journey", "org": "FIFA", "date": date(2024, 7, 1)},
            {"name": "Sports Analytics", "org": "Rajasthan Royals", "date": date(2022, 9, 1)},
            {"name": "Introduction to CP Football Classification", "org": "IFCPF", "date": date(2022, 2, 1)},
            {"name": "Introduction to Cerebral Palsy Football", "org": "IFCPF", "date": date(2022, 2, 1)},
            {"name": "Athletes' Agreement", "org": "IOC", "date": date(2021, 12, 1)},
            {"name": "Marketing Strategy", "org": "Udemy", "date": date(2021, 11, 1)},
            {"name": "Sports Marketing Foundation Course", "org": "Deakin University", "date": date(2021, 11, 1)},
            {"name": "Project Management Course", "org": "Udemy", "date": date(2021, 10, 1)},
            {"name": "Certified Sports Nutritionist", "org": "ACE Fitness", "date": date(2021, 4, 1)},
            {"name": "Sports Nutritionist Certification", "org": "American College of Sports Medicine", "date": date(2020, 3, 1)},
        ]
        
        for cert_data in certifications_data:
            if not Certification.objects.filter(name=cert_data['name']).exists():
                Certification.objects.create(
                    name=cert_data['name'],
                    issuing_organization=cert_data['org'],
                    issue_date=cert_data['date']
                )
        self.stdout.write(self.style.SUCCESS(f'Created {len(certifications_data)} certifications'))
        
        # Create Company Logos (placeholder - will be populated with actual files)
        companies = [
            "Bombay Sharks", "Hyperlink", "India Khelo Football",
            "Jaipur Pink Panthers", "Mumbai City FC", "Mumbai Cricket Association",
            "Pro Govinda", "Rajasthan Royals", "Reckoning eSports",
            "SportVot", "SportsTiger", "Ultimate Table Tennis", "Para Football"
        ]
        
        for i, company in enumerate(companies):
            if not CompanyLogo.objects.filter(company_name=company).exists():
                CompanyLogo.objects.create(
                    company_name=company,
                    order=i,
                    display_on_homepage=True
                )
        self.stdout.write(self.style.SUCCESS(f'Created {len(companies)} company placeholders'))
        
        self.stdout.write(self.style.SUCCESS('\n✓ Portfolio data populated successfully!'))
        self.stdout.write(self.style.WARNING('\nNote: Please upload images through the admin panel at /admin/'))
