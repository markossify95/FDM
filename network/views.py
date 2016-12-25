from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, redirect
from . import models
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@login_required(login_url='/network/login/')
def profile_view(request, id):
    try:
        user = models.User.objects.get(id=id)
        if request.user.userprofile is None:
            print("JEBI!")
        techs = user.usertech_set.get_queryset()
        work_history = user.workhistory_set.get_queryset()
        user_projects = user.userproject_set.get_queryset()
        study_year = "Stariji"
        if user.userprofile.year_of_study != 0:
            study_year = user.userprofile.year_of_study
        learned = []
        to_learn = []
        for t in techs:
            if t.learned:
                learned.append(t)
            else:
                to_learn.append(t)
        context = {
            'user': user,
            'techs': techs,
            'work_history': work_history,
            'user_projects': user_projects,
            'study_year': study_year,
            'learned': learned,
            'to_learn': to_learn
        }
        return render(request, "network/profile.html", context)

    except models.UserProfile.DoesNotExist:
        print('BRAVO, RADI')
        return redirect('/network/profiles/new/' + str(id))
    except models.User.DoesNotExist:
        raise Http404()


@login_required(login_url='/network/login/')
def project_view(request, id):
    if request.user.userprofile is None:
        print("JEBI!")
    project = models.Project.objects.filter(id=id).get()
    members = project.userproject_set.get_queryset()
    context = {
        'project': project,
        'members': members,
    }
    return render(request, "network/project.html", context)


def new_profile(request, id):
    pass


def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated():
            print('TRUE!')
            return redirect('/network/profiles/' + str(request.user.id))
        form = LoginForm()
        context = {
            'form': form
        }

        return render(request, 'network/login.html', context)

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/network/profiles/' + str(user.id))
        return render(request, "network/login.html", context={'form': form})


@login_required(login_url='/network/login/')
def filter_view(request):
    if request.method == "GET":
        if request.user.userprofile is None:
            print("JEBI!")
        tech = models.Tech.objects.all()
        context = {
            'tech': tech
        }
        return render(request, 'network/search.html', context)

    if request.method == "POST":
        if request.user.userprofile is None:
            print("JEBI!")

        data = request.body.decode('utf-8')
        data = data.split('&')
        tech_list = []
        years = []
        status = -1
        for obj in data:
            if "status=" in obj:
                status = obj[-1:]
            elif "tech=" in obj:
                tech_list.append(obj[-1:])
            elif "year=" in obj:
                years.append(obj[-1:])
            else:
                continue
        print(status)
        print('TECH IDs ' + str(tech_list))
        print('YEARS ' + str(years))
        # ime, prezime, username, slika, member-since, xp, top tri tehnologije
        if status != -1:
            users = models.User.objects.filter(userprofile__active__exact=status)
        else:
            users = models.User.objects.all()
        # final = []
        # for u in users:
        #     test = u.user.usertech_set.get_queryset()
        #     test = [t.id for t in test]
        #     print(u.user.username + 'zna: ' + str(test))
        #     if tech_list:
        #         for obj in tech_list:
        #             print(obj)
        #             if obj in test:
        #                 final.append(u)
        #                 break
        #     else:
        #         final = users
        # print(final)
        tech = models.Tech.objects.all()
        print(users)
        context = {'users': users, 'tech': tech, 'status': status, 'years': years}
        return render(request, 'network/search_results.html', context)


def logout_view(request):
    logout(request)
    return redirect('/network/login')
