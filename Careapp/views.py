from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from Careapp.models import Appoinment_index, Appointment,Contact
from datetime import datetime, date

# Create your views here.
def index(request):
    if request.method == 'POST':
        appointment_index = Appoinment_index(

            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],

        )

       
        appointment_index.save()
        messages.success(request, 'Your appointment request has been submitted successfully.')
        return redirect('/')
    else:
        # GET request - just render the template
        return render(request, 'index.html')
    
    

def starter(request):
    return render(request, 'starter-page.html')

def blog(request):
    return render(request, 'blog.html')

def event(request):
    return render(request, 'event.html')

def about(request): 
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def careers(request):
    return render(request, 'careers.html')

def contact(request):
    if request.method == 'POST':
        contact_entry = Contact(
             contactFirstName = request.POST['contactFirstName'],
            contactLastName = request.POST['contactLastName'],
            contactEmail = request.POST['contactEmail'],
            contactPhone = request.POST['contactPhone'],
            contactMessage = request.POST['contactMessage'],
            contactDepartment = request.POST['contactDepartment'],
            contactSubject = request.POST['contactSubject'],
        )

           
        contact_entry.save()
        messages.success(request, 'Your message has been sent successfully.')
        return redirect('/contact')
    else:
        return render(request, 'contact.html')  


def appointment(request):
    if request.method == 'POST':
        try:
            # Get form data
            first_name = request.POST.get('first_name', '').strip()
            last_name = request.POST.get('last_name', '').strip()
            email = request.POST.get('email', '').strip()
            phone_number = request.POST.get('phone_number', '').strip()
            date_of_birth_str = request.POST.get('date_of_birth', '')
            gender = request.POST.get('gender', '')
            department = request.POST.get('department', '')
            preferred_doctor = request.POST.get('preferred_doctor', '').strip()
            preferred_date_str = request.POST.get('preferred_date', '')
            preferred_time = request.POST.get('preferred_time', '')
            appointment_type = request.POST.get('appointment_type', '')
            reason_for_visit = request.POST.get('reason_for_visit', '').strip()
            current_symptoms = request.POST.get('current_symptoms', '').strip()
            current_medications = request.POST.get('current_medications', '').strip()
            insurance_provider = request.POST.get('insurance_provider', '').strip()
            insurance_id = request.POST.get('insurance_id', '').strip()
            terms_accepted = bool(request.POST.get('terms_accepted'))
            communication_consent = bool(request.POST.get('communication_consent'))

            # Validate required fields
            required_fields = {
                'First Name': first_name,
                'Last Name': last_name,
                'Email': email,
                'Phone Number': phone_number,
                'Date of Birth': date_of_birth_str,
                'Gender': gender,
                'Department': department,
                'Preferred Date': preferred_date_str,
                'Preferred Time': preferred_time,
                'Appointment Type': appointment_type,
                'Reason for Visit': reason_for_visit,
            }
            
            missing_fields = [field for field, value in required_fields.items() if not value]
            
            if not terms_accepted:
                missing_fields.append('Terms Acceptance')
            if not communication_consent:
                missing_fields.append('Communication Consent')
            
            if missing_fields:
                messages.error(request, f'Please fill in all required fields: {", ".join(missing_fields)}')
                return render(request, 'appointment.html')

            # Convert date strings to date objects
            try:
                date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
                preferred_date = datetime.strptime(preferred_date_str, '%Y-%m-%d').date()
            except ValueError:
                messages.error(request, 'Invalid date format. Please use the date picker.')
                return render(request, 'appointment.html')

            # Validate dates
            if preferred_date < date.today():
                messages.error(request, 'Appointment date cannot be in the past.')
                return render(request, 'appointment.html')
            
            if date_of_birth > date.today():
                messages.error(request, 'Date of birth cannot be in the future.')
                return render(request, 'appointment.html')

            # Create and save appointment
            appointment = Appointment(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                date_of_birth=date_of_birth,
                gender=gender,
                department=department,
                preferred_doctor=preferred_doctor,
                preferred_date=preferred_date,
                preferred_time=preferred_time,
                appointment_type=appointment_type,
                reason_for_visit=reason_for_visit,
                current_symptoms=current_symptoms,
                current_medications=current_medications,
                insurance_provider=insurance_provider,
                insurance_id=insurance_id,
                terms_accepted=terms_accepted,
                communication_consent=communication_consent,
                status='pending'
            )
            
            appointment.save()
            
            messages.success(request, 'Thank you! Your appointment request has been submitted. We will contact you shortly to confirm your appointment.')
            return redirect('appointment')
            
        except Exception as e:
            messages.error(request, f'An error occurred while processing your appointment: {str(e)}')
            return render(request, 'appointment.html')
    
    else:
        # GET request - show empty form
        return render(request, 'appointment.html')

def billing(request):
    return render(request, 'billing.html')

def departments(request):
    return render(request, 'departments.html')

def doctors(request):
    return render(request, 'doctors.html')

def faq(request):
    return render(request, 'faq.html')

def healthTips(request):
    return render(request, 'healthTips.html')

def insuranceInfo(request):
    return render(request, 'insuranceInfo.html')

def medicalRecords(request):
    return render(request, 'medicalRecords.html')

def patientForms(request):
    return render(request, 'patientForms.html')

def show(request):
    appointment_index = Appoinment_index.objects.all().order_by('-id')

    # Send the data to the template
    context = {
        'appointment_index': appointment_index
    }

    return render(request, 'show.html', context)


def edit(request, id):
           
        
       editappointment=get_object_or_404(Appoinment_index, id=id)

       if request.method == 'POST':
            editappointment.name = request.POST.get('name')
            editappointment.email = request.POST.get('email')
            editappointment.phone = request.POST.get('phone')
            editappointment.date = request.POST.get('date')
            editappointment.department = request.POST.get('department')
            editappointment.doctor = request.POST.get('doctor')
            editappointment.message = request.POST.get('message')

            editappointment.save()
            messages.success(request, 'Your appointment has been updated successfully.')
            return redirect('/show')
       else:
            context = {
                'editappointment': editappointment
            }
            return render(request, 'edit.html', context)   

def delete(request, id):
        
        myappoint= Appoinment_index.objects.get(id = id)
        myappoint.delete()
        messages.success(request, 'Appointment deleted successfully.')
        return redirect('/show')

def register(request):
    return render(request, 'register.html')


    








