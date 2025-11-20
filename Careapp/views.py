from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')