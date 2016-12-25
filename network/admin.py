from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Project)
admin.site.register(models.UserProject)
admin.site.register(models.Tech)
admin.site.register(models.UserTech)
admin.site.register(models.WorkHistory)
