from django.http.response import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.
def profile_view(request, id):
    if request.method == 'GET':
        user = models.User.objects.get(id=id)
        techs = user.usertech_set.get_queryset()
        work_history = user.workhistory_set.get_queryset()
        user_projects = user.userproject_set.get_queryset()
        context = {
            "user": user,
            "techs": techs,
            "work_history": work_history,
            "user_projects": user_projects,
        }
        return render(request, template_name="network/profile.html", context=context)


