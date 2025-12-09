# Sumedh Rajarshi - Professional Portfolio

A premium Django portfolio website with exceptional UI/UX, smooth animations, and complete admin panel management.

## Features

- ✨ **Premium Dark Theme** - Modern sports-inspired design with purple/blue gradients
- 🎨 **Smooth Animations** - Scroll-triggered fade-ins, parallax effects, and 3D hover interactions
- 📱 **Fully Responsive** - Optimized for all devices (mobile, tablet, desktop)
- 🎯 **Admin Panel** - Manage all content through Django admin interface
- 🖼️ **Image Management** - Upload and manage photos, logos, and certificates
- 📧 **Contact & Enrollment Form** - Dual-purpose form for general inquiries and academy enrollments
- ⚡ **Performance Optimized** - Fast loading with lazy-loaded images and GPU-accelerated animations

## Sections

1. **Hero** - Full-screen introduction with profile photo
2. **About Me** - Professional bio and social media links
3. **Experience** - Interactive timeline of work history
4. **Bombay Sharks Academy** - Dedicated section for football academy
5. **Certifications** - Grid display of credentials and courses
6. **Companies** - Showcase of companies worked with
7. **Contact** - Form for general contact and academy enrollment

## Setup Instructions

### Prerequisites

- Python 3.13+ installed
- Virtual environment (recommended)

### Installation

1. **Navigate to project directory:**
   ```bash
   cd /Users/vinayadusumilli/sumedh_rajarshi
   ```

2. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies** (already installed):
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** (already done):
   ```bash
   python manage.py migrate
   ```

5. **Populate initial data** (already done):
   ```bash
   python manage.py populate_data
   ```

6. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the website:**
   - Website: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

## Admin Panel Usage

### First Login

1. Go to http://localhost:8000/admin
2. Login with your superuser credentials
3. Start managing content!

### Managing Content

#### About Me
- Upload profile photo
- Update bio, contact information
- Add social media links
- Upload CV/Resume

#### Experiences
- Add new work experiences
- Upload company logos
- Set display order
- Mark current positions

#### Bombay Sharks Academy
- Update academy description
- Upload hero image
- Add gallery images
- Manage academy details

#### Certifications
- Add new certifications
- Upload certificate badges
- Set issue dates and credentials

#### Companies
- Upload company logos
- Toggle homepage display
- Set display order

#### Contact Submissions
- View all form submissions
- Mark as read/unread
- Add admin notes
- Track enrollment inquiries

## Image Guidelines

For best results, use these image specifications:

- **Profile Photo**: Square (1:1 ratio), min 500x500px
- **Company Logos**: PNG with transparency, max 300x300px
- **Hero Images**: Landscape (16:9 ratio), min 1920x1080px
- **Certificates**: Any size, will be auto-resized

## Technologies Used

- **Backend**: Django 6.0
- **Frontend**: HTML5, CSS3 (Custom), JavaScript (Vanilla)
- **Rich Text**: CKEditor
- **Database**: SQLite (development)
- **Fonts**: Google Fonts (Inter)
- **Icons**: Font Awesome 6

## Project Structure

```
sumedh_rajarshi/
├── portfolio_project/      # Django project settings
├── portfolio/              # Main portfolio app
│   ├── models.py          # Database models
│   ├── views.py           # Views and logic
│   ├── admin.py           # Admin configuration
│   ├── forms.py           # Form definitions
│   └── management/        # Custom commands
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── media/                 # Uploaded files
├── Logos/                 # Original logo files
├── Personal Photos/       # Original photos
└── manage.py              # Django management script
```

## Customization

### Changing Colors

Edit `/static/css/main.css` and modify the CSS custom properties:

```css
:root {
    --color-primary: #6366f1;    /* Primary purple */
    --color-secondary: #8b5cf6;   /* Secondary purple */
    --color-accent: #06b6d4;      /* Accent cyan */
}
```

### Adding New Sections

1. Create new model in `portfolio/models.py`
2. Register in `portfolio/admin.py`
3. Add to view in `portfolio/views.py`
4. Update template in `templates/portfolio/home.html`
5. Add styles in `static/css/components.css`

## Deployment

### Production Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL database
- [ ] Configure static files serving
- [ ] Set up media files serving
- [ ] Enable HTTPS
- [ ] Set strong `SECRET_KEY`

## Support

For issues or questions, contact Sumedh Rajarshi.

## License

© 2025 Sumedh Rajarshi. All rights reserved.
