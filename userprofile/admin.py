from django.contrib import admin
from .models import Profile, Education, Experience, Skill

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)


from .models import Profile, Education, Experience, Skill, Project

admin.site.register(Project)

from .models import ContactMessage

admin.site.register(ContactMessage)