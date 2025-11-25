from django.contrib import admin
from Careapp.models import Patient,MedicalRecord, Appointment,Appoinment_index

# Register your models here.

admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
admin.site.register(Appoinment_index)