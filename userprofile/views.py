from django.shortcuts import render
from .models import Profile, Education, Experience, Skill

def home(request):
    profile = Profile.objects.first()
    return render(request, 'userprofile/home.html', {'profile': profile})


def about(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()

    return render(request, 'userprofile/about.html', {
        'education': education,
        'experience': experience,
        'skills': skills
    })


from .models import Project

def projects(request):
    projects = Project.objects.all()
    return render(request, 'userprofile/projects.html', {'projects': projects})


from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, 'userprofile/contact.html')