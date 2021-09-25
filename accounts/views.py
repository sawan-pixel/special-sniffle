from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserAdminCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('List_Page')

    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})


def details_view(request):
    post_data = CustomUser.objects.all()
    return render(request, 'List_Page.html', {'post': post_data})


def update_data(request, id):
    if request.method == 'POST':
        pi = CustomUser.objects.get(pk=id)
        fm = UserAdminCreationForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('List_Page')
    else:
        pi = CustomUser.objects.get(pk=id)
        fm = UserAdminCreationForm(instance=pi)
    return render(request, 'update_data.html', {'form': fm})


def delete(request, id):
    if request.method == 'POST':
        pi = CustomUser.objects.get(pk=id)
        pi.delete()
        return redirect('List_Page')


def user_logout(request):
    logout(request)
    return HttpResponse("<h1>Thanks for spending some quality time with the Web site today.</h1>")
