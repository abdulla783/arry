from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from resume.models import Home, Contact
from django.http import FileResponse
import os
from django.contrib import messages


# Create your views here.


def home(request):
    context = {
        'file': Home.objects.all()
        }
    return render(request, 'resume/home.html', context)

def download_pdf(request):
    filename = 'Arif_Resume.pdf'
    filepath = os.path.join('media', 'cv', filename)
    # Read the PDF file from the database or file system
    # and return it as a FileResponse
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def about(request):
    return render(request, 'resume/about.html')


def service(request):
    return render(request, 'resume/service.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        subject = request.POST.get('subject', '')
        requirement = request.POST.get('requirement', '')
        
        if Contact.objects.filter(email=email, contact=contact).exists():
                messages.error(request, 'You have already filled the form.')
                return render(request, 'resume/contact.html')
        else:
            # Save the form data to the database
            # print(name, email, contact, subject, requirement)
            contact = Contact(name=name, email=email, contact=contact, subject=subject, requirement=requirement)
            contact.save()
            messages.error(request, 'Message has been sent successfuly.')
            return render(request, 'resume/contact.html')
        
    return render(request, 'resume/contact.html',)

def termCon(request):
     return render(request, 'resume/termCon.html')
