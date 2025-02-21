from django.http import JsonResponse
from django.shortcuts import render
from .models import ContactInfo, ContactMessage
from django.shortcuts import render, redirect
from .models import Review
from .forms import ContactMessageForm, ReviewForm

from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from .models import ServiceCategory, Service, SiteImage



def cyber_services(request):
    return render(request, 'cyber_services.html')

def entertainment(request):
    return render(request, 'entertainment.html')

def graphics_design(request):
    return render(request, 'graphics_design.html')

def construction(request):
    return render(request, 'construction.html')

def contact(request):
    contact_info = ContactInfo.objects.first()
    return render(request, 'contact.html', {'contact_info': contact_info})


def home(request):
    contact_info = ContactInfo.objects.first()
    reviews = Review.objects.all()

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Your message has been sent successfully!"})
        else:
            return JsonResponse({"success": False, "message": "Please fill all fields correctly."})

    else:
        form = ContactMessageForm()

    return render(request, 'index.html', {'contact_info': contact_info, 'reviews': reviews, 'form': form})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'index.html', {'form': form})



def category_images(request, category_name):
    category = get_object_or_404(ServiceCategory, name=category_name)
    services = Service.objects.filter(category=category)
    images = SiteImage.objects.filter(category=category)
    
    context = {
        'category': category,
        'services': services,
        'images': images
    }
    return render(request, 'category_images.html', context)


def contact_page(request):
    # Fetch the first contact info entry or set a default
    contact_info = ContactInfo.objects.first()
    if not contact_info:
        contact_info = ContactInfo(
            email="samamwa13@gmail.com",
            phone="+254715825808",
            whatsapp="+254700123456"
        )

    return render(request, 'base.html', {'contact_info': contact_info})
