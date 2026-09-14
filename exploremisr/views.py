from django.shortcuts import render, redirect
from django.contrib import messages

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
