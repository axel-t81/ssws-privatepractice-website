from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = f'New Contact Form Submission from {name}'
            email_message = f"""
            You have received a new contact form submission:
            
            Name: {name}
            Email: {email}
            Message:
            {message}
            """
            
            try:
                send_mail(
                    subject=subject,
                    message=email_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['kojrey@kojreycodes.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message! We will get back to you soon.')
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again later.')
            
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'home.html', {'form': form})