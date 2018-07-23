# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileFrom


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        # 验证所传数据是否合法
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Welcome You. You have been authenticated successfully")
            else:
                return HttpResponse("Invalid login")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})


# def register(request):
#     if request.method == "POST":
#         user_form = RegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)  # 创建数据对象，不保存到数据库
#             new_user.set_password(user_form.cleaned_data["password"])  # 设置密码
#             new_user.save()  # 保存到数据库中
#             return HttpResponse("successfully")
#         else:
#             return HttpResponse("sorry, you can not register")
#     else:
#         user_form = RegistrationForm()
#         return render(request, "account/register.html", {"form": user_form})


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileFrom(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, you can not register.")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileFrom()
        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form})

