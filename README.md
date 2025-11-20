Medilab Healthcare – Django Medical Website
<p align="center"> <img src="https://img.shields.io/badge/Medilab-Healthcare-blue"> <img src="https://img.shields.io/badge/Django-4.2-green"> <img src="https://img.shields.io/badge/Bootstrap-5.3-purple"> <img src="https://img.shields.io/badge/Design-Responsive-success"> </p>

A modern, fully responsive healthcare website built with Django and Bootstrap featuring medical services, departments, doctor profiles, and appointment booking.

🏥 Overview

Medilab Healthcare provides a professional online presence for hospitals, clinics, and medical organizations.
The template includes appointment booking, dynamic sections, and a clean, mobile-friendly UI.

✨ Features
✔ Core Features

Medical Services Showcase

Doctor Profiles

Appointment Booking

Department Information

FAQs & Patient Resources

🎨 Design Features

Responsive & Mobile-Friendly

Modern UI/UX

Smooth Animations (AOS)

Fast & Lightweight

💼 Business Features

Contact Page + Google Map

Testimonials

Image Gallery

Service Catalog

🛠 Tech Stack

Backend: Django 4.2, Python 3.8+
Frontend: HTML5, CSS3, JavaScript, Bootstrap 5.3
Database: SQLite (dev) / PostgreSQL (prod)
Libraries: AOS, Swiper.js, Glightbox, PureCounter

📂 Project Structure
medilab-django/
│
├── medilab/            # Project settings
├── mainapp/            # Main application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── index.html
│       └── services.html
│
├── static/             # CSS, JS, images
└── templates/          # Base templates

🚀 Installation
1. Clone the Project
git clone https://github.com/yourusername/medilab-django.git
cd medilab-django

2. Create Virtual Environment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Migrate Database
python manage.py migrate

5. Run the Development Server
python manage.py runserver


Open in browser:
👉 http://localhost:8000

⚙️ Environment Variables

Create a .env file:

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1

🧩 Key Models
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to="doctors/")

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

🖌️ Customization
Change Colors (static/assets/css/main.css)
:root {
  --primary: #0d6efd;
  --secondary: #6c757d;
  --medical-blue: #1976d2;
}

Add a Service Card
<div class="service-item">
  <i class="fas fa-heartbeat"></i>
  <h3>Cardiology</h3>
  <p>Advanced heart care and diagnostics.</p>
</div>

🌐 Deployment
PostgreSQL Setup
CREATE DATABASE medilab;
CREATE USER medilabuser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE medilab TO medilabuser;


Deployable on:
✔ Heroku
✔ DigitalOcean
✔ PythonAnywhere
✔ AWS EC2

🤝 Contributing

Fork the repo

Create a branch

Commit changes

Push

Open a Pull Request

📄 License

This project is licensed under the MIT License.

Template Credit: BootstrapMade
Icons: Font Awesome, Bootstrap Icons

❤️ Medilab Healthcare

Built with Django + Bootstrap