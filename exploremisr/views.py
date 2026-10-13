from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Global list to store waitlist entries in memory
WAITLIST_NUMBERS = []

def index(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        if mobile_number:
            WAITLIST_NUMBERS.append(mobile_number)
            messages.success(request, 'Thank you! You have been added to the waitlist.')
            return redirect('/#waitlist')
    return render(request, 'index.html')

def manage_waitlist(request):
    return render(request, 'manage.html', {'numbers': WAITLIST_NUMBERS})

def google_verification(request):
    return HttpResponse('google-site-verification: googlec1b82d93b0cf05b2.html', content_type='text/html')
