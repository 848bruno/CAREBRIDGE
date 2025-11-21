from django.shortcuts import render

# Create your views here.
def index(request):
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
    return render(request, 'contact.html')  

def appointment(request):
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



