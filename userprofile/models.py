from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.institution


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.company


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name