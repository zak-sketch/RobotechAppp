from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Service, Blog, EducationProject, TeamMember

def home(request):
    return render(request, 'home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def blog(request):
    blogs = Blog.objects.all().order_by('-published_date')
    return render(request, 'blog.html', {'blogs': blogs})

def education(request):
    projects = EducationProject.objects.all()
    team_members = TeamMember.objects.all()
    return render(request, 'education.html', {'projects': projects, 'team_members': team_members})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Optional: Save to DB or email logic
        print(f"New Contact: {name}, {email}, {message}")

        messages.success(request, "Your message has been sent!")
        return redirect('contact')  # Optional: Replace with a thank-you page

    return render(request, 'contact.html')
