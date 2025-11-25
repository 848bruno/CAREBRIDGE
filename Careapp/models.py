from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateField()
    description = models.TextField()
    document = models.FileField(upload_to='medical_records/')

    def __str__(self):
        return f"Record for {self.patient} on {self.record_date}"


class Appointment(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    date_of_birth = models.DateField()
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('prefer-not-to-say', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    
    # Appointment Details
    DEPARTMENT_CHOICES = [
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('dermatology', 'Dermatology'),
        ('internal-medicine', 'Internal Medicine'),
        ('surgery', 'Surgery'),
        ('emergency', 'Emergency Medicine'),
    ]
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    
    DOCTOR_CHOICES = [
        ('', 'Any Available Doctor'),
        ('dr-johnson', 'Dr. Sarah Johnson (Cardiology)'),
        ('dr-chen', 'Dr. Michael Chen (Neurology)'),
        ('dr-rodriguez', 'Dr. Emily Rodriguez (Internal Medicine)'),
        ('dr-wilson', 'Dr. James Wilson (Orthopedics)'),
        ('dr-jepson', 'Dr. Amanda Jepson (Pediatrics)'),
    ]
    preferred_doctor = models.CharField(max_length=50, choices=DOCTOR_CHOICES, blank=True)
    
    preferred_date = models.DateField()
    
    TIME_SLOT_CHOICES = [
        ('08:00', '8:00 AM'),
        ('08:30', '8:30 AM'),
        ('09:00', '9:00 AM'),
        ('09:30', '9:30 AM'),
        ('10:00', '10:00 AM'),
        ('10:30', '10:30 AM'),
        ('11:00', '11:00 AM'),
        ('11:30', '11:30 AM'),
        ('13:00', '1:00 PM'),
        ('13:30', '1:30 PM'),
        ('14:00', '2:00 PM'),
        ('14:30', '2:30 PM'),
        ('15:00', '3:00 PM'),
        ('15:30', '3:30 PM'),
        ('16:00', '4:00 PM'),
        ('16:30', '4:30 PM'),
    ]
    preferred_time = models.CharField(max_length=5, choices=TIME_SLOT_CHOICES)
    
    APPOINTMENT_TYPE_CHOICES = [
        ('consultation', 'New Patient Consultation'),
        ('follow-up', 'Follow-up Visit'),
        ('routine-checkup', 'Routine Check-up'),
        ('emergency', 'Emergency Visit'),
        ('telemedicine', 'Telemedicine Consultation'),
        ('procedure', 'Medical Procedure'),
    ]
    appointment_type = models.CharField(max_length=20, choices=APPOINTMENT_TYPE_CHOICES)
    
    # Medical Information
    reason_for_visit = models.TextField()
    current_symptoms = models.TextField(blank=True)
    current_medications = models.TextField(blank=True)
    
    # Insurance Information
    insurance_provider = models.CharField(max_length=100, blank=True)
    insurance_id = models.CharField(max_length=50, blank=True)
    
    # Terms and Consent
    terms_accepted = models.BooleanField()
    communication_consent = models.BooleanField()
    
    # Status and Metadata
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirmation_sent = models.BooleanField(default=False)
    notes = models.TextField(blank=True, help_text="Internal notes about the appointment")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.preferred_date} {self.preferred_time}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def is_upcoming(self):
        """Check if the appointment is in the future"""
        appointment_datetime = timezone.make_aware(
            timezone.datetime.combine(self.preferred_date, 
                                    timezone.datetime.strptime(self.preferred_time, '%H:%M').time())
        )
        return appointment_datetime > timezone.now()
    
    def get_appointment_datetime(self):
        """Return the full datetime of the appointment"""
        return timezone.make_aware(
            timezone.datetime.combine(self.preferred_date, 
                                    timezone.datetime.strptime(self.preferred_time, '%H:%M').time())
        )   




    
    
