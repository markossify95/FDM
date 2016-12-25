from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)
    year_of_study = models.IntegerField(default=0)
    about = models.TextField(max_length=10000)
    phone = models.CharField(max_length=15, default="N/A")
    xp = models.IntegerField(default=0)
    pic_url = models.URLField(blank=True, null=True)
    git_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Tech(models.Model):
    tech_name = models.CharField(max_length=250)

    def __str__(self):
        return self.tech_name


class UserTech(models.Model):
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, default="")  # Konkretno sta je u pitanju
    learned = models.BooleanField(default=False)  # 1 - nauceno, 0 - tek uci

    def __str__(self):
        return self.user.username + ": " + self.tech.tech_name


class WorkHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250, blank=False, null=False)
    position = models.CharField(max_length=250, blank=False, null=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.user.username + " - " + self.company_name + ": " + self.position


class Project(models.Model):
    project_name = models.CharField(max_length=250, blank=False, null=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.project_name


class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, default="letac", blank=False)
    description = models.TextField(max_length=5000, blank=True, null=True)
    xp_value = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + " on: " + self.project.project_name
