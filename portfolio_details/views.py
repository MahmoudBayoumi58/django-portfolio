from django.shortcuts import render
from portfolio_details.models import *


# Create your views here.
def home_view(request):
    page_name = 'index'
    info = PersonalInfo.objects.first()
    context_data = {
        'page_name': page_name,
        'info': info
    }
    return render(request, 'portfolio/home.html', context=context_data)


def about_view(request):
    page_name = 'about'
    info = PersonalInfo.objects.first()
    skills = Skill.objects.all()
    certificates = Certificate.objects.all()
    context_data = {
        'page_name': page_name,
        'info': info,
        'skills': skills,
        'certificates': certificates,
    }
    return render(request, 'portfolio/about.html', context=context_data)


def resume_view(request):
    page_name = 'resume'
    info = PersonalInfo.objects.first()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    context_data = {
        'page_name': page_name,
        'info': info,
        'educations': educations,
        'experiences': experiences,
    }
    return render(request, 'portfolio/resume.html', context=context_data)


def portfolio_view(request):
    page_name = 'portfolio'
    info = PersonalInfo.objects.first()
    projects = Project.objects.all()
    context_data = {
        'page_name': page_name,
        'info': info,
        'projects': projects,
    }
    return render(request, 'portfolio/portfolio.html', context=context_data)


def portfolio_details(request, pk):
    page_name = 'portfolio-details'
    info = PersonalInfo.objects.first()
    project = Project.objects.get(pk=pk)
    context_data = {
        'page_name': page_name,
        'info': info,
        'project': project,
    }
    return render(request, 'portfolio/portfolio-details.html', context=context_data)


def contact_view(request):
    page_name = 'contact'
    info = PersonalInfo.objects.first()
    context_data = {
        'page_name': page_name,
        'info': info,
    }
    return render(request, 'portfolio/contact.html', context=context_data)


def services_view(request):
    page_name = 'services'
    info = PersonalInfo.objects.first()
    services = Service.objects.all()
    context_data = {
        'page_name': page_name,
        'info': info,
        'services': services,
    }
    return render(request, 'portfolio/services.html', context=context_data)
