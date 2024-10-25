from django.shortcuts import render, redirect
from .models import QRCode
from .utils import generate_qr_code
from django.contrib.auth.decorators import login_required
# Form 

from django import forms

class QRCodeForm(forms.Form):
    text= forms.CharField(widget=forms.Textarea, label='Enter Text')

@login_required
def generate_qr(request):
    if request.method== 'POST':
        form= QRCodeForm(request.POST)
        if form.is_valid():
            text= form.cleaned_data['text']
            qr_code_file= generate_qr_code(text)
            qr_code= QRCode(user= request.user, text= text, qr_code_image= qr_code_file)
            qr_code.save()
            return redirect('qr_list')
    else:
        form= QRCodeForm()
    return render(request, 'generate_qr.html', {'form':form})

@login_required
def qr_list(request):
    qr_codes= QRCode.objects.filter(user=request.user)
    return render(request, 'qr_list.html', {'qr_codes': qr_codes})