from django.shortcuts import render, redirect
from .forms import QRForm
from .models import QR, QRImage

# Create your views here.

def generate_qr(request):
    
    pass

def home(request):
    form= QRForm()
    if request.method=='POST':
        form= QRForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context= {
        'form':form
    }
    return render(request, 'home.html', context)