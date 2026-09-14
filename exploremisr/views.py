import re
from pathlib import Path

from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import redirect, render

# In-memory waitlist (Vercel serverless has a read-only filesystem, so no DB)
WAITLIST_NUMBERS = []

VERIFICATION_DIR = Path(__file__).resolve().parent.parent / 'verification'


def google_verification(request):
    return FileResponse(
        open(VERIFICATION_DIR / 'googlec1b82d93b0cf05b2.html', 'rb'),
        content_type='text/html',
    )


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
        elif mobile_number in WAITLIST_NUMBERS:
            messages.info(request, 'This number is already on the waitlist.')
        else:
            WAITLIST_NUMBERS.append(mobile_number)
            messages.success(request, 'Thank you! You have been added to the waitlist.')
        return redirect('/#waitlist')
    return render(request, 'index.html')


def manage_waitlist(request):
    return render(request, 'manage.html', {'numbers': WAITLIST_NUMBERS})