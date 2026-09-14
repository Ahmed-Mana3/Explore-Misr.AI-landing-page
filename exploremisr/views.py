import re

from django.contrib import messages
from django.shortcuts import redirect, render

from waitlist.models import WaitlistEntry


def normalize_mobile_number(value):
    number = re.sub(r'[\s\-()]', '', value or '').strip()
    if not re.fullmatch(r'\+?\d{8,15}', number):
        return None
    return number


def index(request):
    if request.method == 'POST':
        mobile_number = normalize_mobile_number(request.POST.get('mobile_number'))
        if not mobile_number:
            messages.error(request, 'Please enter a valid mobile number.')
        elif WaitlistEntry.objects.filter(mobile_number=mobile_number).exists():
            messages.info(request, 'This number is already on the waitlist.')
        else:
            WaitlistEntry.objects.create(mobile_number=mobile_number)
            messages.success(request, 'Thank you! You have been added to the waitlist.')
        return redirect('/#waitlist')
    return render(request, 'index.html')


def manage_waitlist(request):
    numbers = WaitlistEntry.objects.order_by('created_at')
    return render(request, 'manage.html', {'numbers': numbers})