from django.shortcuts import render, redirect
from django.contrib import messages
from waitlist.models import WaitlistEntry

def index(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        if mobile_number:
            WaitlistEntry.objects.create(mobile_number=mobile_number)
            messages.success(request, 'Thank you! You have been added to the waitlist.')
            return redirect('/#waitlist')
    return render(request, 'index.html')
