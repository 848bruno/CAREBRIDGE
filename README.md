Medilab Healthcare – Django Medical Website








A comprehensive, responsive medical website built with Django featuring healthcare services, department information, doctor profiles, and an appointment booking system.

🏥 Project Overview

Medilab is a professional medical website template designed for hospitals, clinics, and healthcare providers.
It offers a modern UI/UX with essential features such as service listings, doctor profiles, booking appointments, and patient resources.

✨ Features
🎯 Core Features

Medical Service Showcase – Highlight healthcare services & specialties

Doctor Profiles – Medical team profiles with credentials

Appointment Booking System – Online appointment scheduling

Department Information – Specialized medical departments

Patient Resources – FAQ, health tips, educational content

🎨 Design Features

Fully Responsive — Optimized for all devices

Modern UI/UX

Fast Loading & optimized performance

Accessible — Web accessibility-friendly

💼 Business Features

Contact Integration (email, phone, Google Maps)

Service Catalog

Testimonials

Gallery Showcase

🛠️ Technology Stack
Backend

Django 4.2+

Python 3.8+

SQLite (Dev) / PostgreSQL (Production)

Frontend

HTML5

CSS3

JavaScript

Bootstrap 5.3

Bootstrap Icons & Font Awesome

Additional Libraries

AOS (Animate on Scroll)

Swiper.js

Glightbox

PureCounter

📁 Project Structure
medilab-django/
├── manage.py
├── requirements.txt
├── medilab/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── mainapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── index.html
│       ├── services.html
│       └── base.html
├── static/
│   ├── assets/
│   │   ├── css/
│   │   ├── js/
│   │   ├── img/
│   │   └── vendor/
└── templates/
    ├── base.html
    └── pages/

🚀 Installation & Setup
Prerequisites

Python 3.8+

pip

Virtualenv (recommended)

1. Clone the Repository
git clone https://github.com/yourusername/medilab-django.git
cd medilab-django

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
cp .env.example .env


Edit .env:

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1

5. Run Migrations
python manage.py migrate

6. Collect Static Files
python manage.py collectstatic

7. Create Superuser
python manage.py createsuperuser

8. Start Server
python manage.py runserver


Visit:

http://localhost:8000

⚙️ Configuration
Static & Media Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

Template Settings
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
    },
]

📱 Pages & Sections
Main Pages

Home

About

Services

Departments

Doctors

Contact

Components

Header & Hero Section

Appointment Form

Testimonials

FAQ

Footer

🎨 Customization
Add New Service
<div class="service-item">
  <div class="icon"><i class="fas fa-heartbeat"></i></div>
  <h3>Cardiology</h3>
  <p>Comprehensive heart care and interventions.</p>
</div>

Custom Colors (main.css)
:root {
  --primary-color: #0d6efd;
  --medical-blue: #1976d2;
}

📊 Database Models (Sample)
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctors/')

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

🚀 Deployment
PostgreSQL Setup
CREATE DATABASE medilab;
CREATE USER medilabuser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE medilab TO medilabuser;

Production DATABASES Setting
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'medilab',
        'USER': 'medilabuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
    }
}

Deployment Options

Heroku

PythonAnywhere

AWS EC2

DigitalOcean

🤝 Contributing

Fork the repo

Create a branch:
git checkout -b feature/NewFeature

Commit:
git commit -m "Add NewFeature"

Push:
git push origin feature/NewFeature

Open a Pull Request

🐛 Troubleshooting
Issue	Solution
Static files not loading	Run collectstatic
Template errors	Check template paths
Database issues	Run migrations
Django compatibility	Update Django version
📄 License

Licensed under the MIT License.

Template Attribution

UI Template: BootstrapMade

Icons: Bootstrap Icons & Font Awesome

👥 Target Audience

Hospitals

Clinics

Healthcare centers

Medical professionals

📞 Support

GitHub Issues

Email: support@medilab.com

🔄 Changelog
v1.0.0

Initial release

Responsive UI

Appointment system

Doctor & department profiles