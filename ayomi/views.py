from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from ayomi.models import UserDataAccessObject, UserDataAccessException

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect("main_view")


def do_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("main_view")
    else:
        return redirect("login_view")


def login_view(request):
    return render(request, "login.html")

@login_required
def main(request):
    user = UserDataAccessObject(request.user)
    return render(request, "main.html", user.__dict__())


def modify_email(request, **kwargs):
    user = UserDataAccessObject(request.user)
    if not user:
        raise Http404

    try:
        user.set_email(kwargs['email'])
        user.save()
    except UserDataAccessException:
        # Which means we have no user
        raise Http404

    return JsonResponse({"status": True, "email": kwargs['email']})


def modify_first_name(request, **kwargs):
    user = UserDataAccessObject(request.user)

    if not user:
        raise Http404

    try:
        user.set_first_name(kwargs['first_name'])
        user.save()
    except UserDataAccessException:
        # Which means we have no user
        raise Http404

    return JsonResponse({"status": True, "first_name": kwargs['first_name']})


def modify_last_name(request, **kwargs):
    user = UserDataAccessObject(request.user)

    if not user:
        raise Http404

    try:
        user.set_last_name(kwargs['last_name'])
        user.save()
    except UserDataAccessException:
        # Which means we have no user
        raise Http404

    return JsonResponse({"status": True, "last_name": kwargs['last_name']})
