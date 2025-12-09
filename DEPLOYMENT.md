# Deployment Guide - PythonAnywhere

## Prerequisites
- PythonAnywhere account (free or paid)
- GitHub repository with the code
- Admin credentials for Django

## Step 1: Clone Repository on PythonAnywhere

1. **Login to PythonAnywhere**: https://www.pythonanywhere.com
2. **Open a Bash Console** from the Dashboard
3. **Clone your repository**:
```bash
git clone https://github.com/vinayadusumillli/Sumedh_Rajarshi.git
cd Sumedh_Rajarshi
```

## Step 2: Set Up Virtual Environment

```bash
# Create virtual environment with Python 3.10 (PythonAnywhere default)
mkvirtualenv --python=/usr/bin/python3.10 sumedh_portfolio

# Activate virtual environment (it should auto-activate after creation)
workon sumedh_portfolio

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Configure Django Settings

1. **Create `.env` file**:
```bash
nano .env
```

2. **Add these settings** (replace with your values):
```
SECRET_KEY=your-very-secure-random-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
```

3. **Generate a new SECRET_KEY**:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Step 4: Database Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Populate initial data
python manage.py populate_data

# Upload images
python manage.py upload_images

# Collect static files
python manage.py collectstatic --noinput
```

## Step 5: Configure Web App on PythonAnywhere

1. **Go to Web Tab** on PythonAnywhere Dashboard
2. **Click "Add a new web app"**
3. **Choose "Manual configuration"**
4. **Select Python 3.10**

### Configure WSGI File

1. Click on **WSGI configuration file** link
2. Replace the content with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/Sumedh_Rajarshi'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'

# Activate virtual environment
activate_this = '/home/yourusername/.virtualenvs/sumedh_portfolio/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Note**: Replace `yourusername` with your PythonAnywhere username

### Configure Virtual Environment

1. In the **Web tab**, scroll to **Virtualenv** section
2. Enter: `/home/yourusername/.virtualenvs/sumedh_portfolio`

### Configure Static Files

1. In the **Web tab**, scroll to **Static files** section
2. Add these mappings:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/yourusername/Sumedh_Rajarshi/staticfiles` |
| `/media/` | `/home/yourusername/Sumedh_Rajarshi/media` |

## Step 6: Update Django Settings for Production

Edit `portfolio_project/settings.py`:

```python
# At the top, add:
from decouple import config

# Update these settings:
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# For production, you might want to add:
SECURE_SSL_REDIRECT = True  # Only if using HTTPS
SESSION_COOKIE_SECURE = True  # Only if using HTTPS
CSRF_COOKIE_SECURE = True  # Only if using HTTPS
```

## Step 7: Reload Web App

1. Go back to the **Web tab**
2. Click the green **Reload** button
3. Your site should now be live at: `https://yourusername.pythonanywhere.com`

## Step 8: Upload Images via Admin

1. Visit: `https://yourusername.pythonanywhere.com/admin`
2. Login with superuser credentials
3. The images were already uploaded via the `upload_images` command
4. You can verify in each section:
   - About Me → Profile photo
   - Company Logos → All logos
   - Bombay Sharks → Hero image and gallery

## Updating Your Site

When you make changes:

```bash
# On PythonAnywhere bash console
cd ~/Sumedh_Rajarshi
git pull origin main
workon sumedh_portfolio
pip install -r requirements.txt  # If dependencies changed
python manage.py migrate  # If models changed
python manage.py collectstatic --noinput  # If static files changed
```

Then reload the web app from the Web tab.

## Troubleshooting

### Check Error Logs
- Web tab → **Error log** link
- Web tab → **Server log** link

### Common Issues

1. **Static files not loading**:
   - Run `python manage.py collectstatic`
   - Check static files mappings in Web tab

2. **ImportError**:
   - Ensure virtual environment is activated
   - Check WSGI file path

3. **Database errors**:
   - Run migrations: `python manage.py migrate`
   - Check database file permissions

4. **Images not displaying**:
   - Check media files mapping in Web tab
   - Verify media files were uploaded
   - Check MEDIA_URL and MEDIA_ROOT settings

## Using Custom Domain (Optional)

For paid PythonAnywhere accounts:
1. Go to **Web tab**
2. Click **Add a new web app**
3. Choose your custom domain
4. Update DNS settings with your domain provider

## Performance Tips

1. **Enable caching** in Django settings
2. **Optimize images** before uploading
3. **Use CDN** for static files (optional)
4. **Upgrade to paid plan** for better performance

## Support

- PythonAnywhere Help: https://help.pythonanywhere.com/
- Django Documentation: https://docs.djangoproject.com/
- GitHub Repository: https://github.com/vinayadusumillli/Sumedh_Rajarshi

---

**Your portfolio is now live! 🎉**
