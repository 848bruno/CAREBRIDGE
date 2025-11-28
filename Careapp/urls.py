
from django.contrib import admin
from django.urls import path
from Careapp import views

urlpatterns =[
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter-page'),
    path('blog/', views.blog, name='blog'),
    path('event/', views.event, name='event'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('billing/', views.billing, name='billing'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('faq/', views.faq, name='faq'),
    path('healthTips/', views.healthTips, name='healthTips'),
    path('insuranceInfo/', views.insuranceInfo, name='insuranceInfo'),
    path('medicalRecords/', views.medicalRecords, name='medicalRecords'),
    path('patientForms/', views.patientForms, name='patientForms'),
    path('show/', views.show, name='show'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),

]
    
