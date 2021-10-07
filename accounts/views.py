from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            logout(request)
            return redirect("/")
        else:
            return redirect("/")
    else:
        return redirect("/")


def register_view(request):
    form = UserCreationForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        user = form.save()
        return redirect("/")
    return render(request, "accounts/register.html", context)