# TeddyPups — Django website clone starter

A multi-page, responsive puppy boutique website built with HTML, CSS, JavaScript, Bootstrap 5, Django and MySQL.

## Features
- Homepage with hero, puppy cards, brand story, process and CTA sections
- Puppies, How It Works, Happy Families, FAQ, Visit & Contact pages
- Responsive Bootstrap navigation and layouts
- Working enquiry form with Django CSRF protection and MySQL persistence
- Django admin for puppy inventory and enquiries
- Demo puppy cards render even before the database is populated

## Requirements
Python 3.10+, MySQL 8+, pip.

## Local setup (Windows PowerShell)
```powershell
py -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Create a MySQL database:
```sql
CREATE DATABASE teddypups_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
Copy `.env.example` to `.env` and set your MySQL credentials. Install `python-dotenv` and add `from dotenv import load_dotenv; load_dotenv(BASE_DIR / '.env')` near the top of `settings.py` if you want automatic `.env` loading, or set environment variables in your terminal.

Then run:
```powershell
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000

## Important customization before submission
1. Replace the placeholder WhatsApp number `971500000000` in `templates/base.html` and `templates/core/contact.html` with the business's verified number.
2. Replace placeholder email/location and demo puppy records/photos with accurate information/assets from the reference website, where permitted.
3. Verify image links load and use locally stored licensed assets for production.
4. Set `DEBUG=False`, a strong `DJANGO_SECRET_KEY`, correct `ALLOWED_HOSTS`, HTTPS and production MySQL credentials.
5. Configure static file serving (`collectstatic`) and a production host such as PythonAnywhere, Render or a VPS with MySQL support.

## Project structure
```
teddypups/
  settings.py urls.py wsgi.py
core/
  models.py views.py admin.py
templates/
  base.html
  core/ (home, puppies, how, families, faq, contact)
static/
  css/style.css
  js/main.js
```

## AI usage disclosure
Record the tools and prompts actually used during your work. Suggested prompt log:
- "Create a responsive multi-page puppy boutique website using Django templates, Bootstrap 5, custom CSS and vanilla JavaScript. Include a homepage, puppy listing, how-it-works, happy families, FAQ and contact pages."
- "Build Django Puppy and Enquiry models using MySQL, register them in admin, and save validated contact form submissions with CSRF protection."
- "Review the responsive layout at 1440px, 768px and 390px widths; identify overflow, navigation and image sizing issues."

This is an independently authored approximation, not a pixel-perfect reproduction. Compare every page against the live reference and replace placeholders before submitting.
