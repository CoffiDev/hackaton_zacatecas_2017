# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from .models import YoungProfile
from django.contrib import messages
from django.contrib.auth import authenticate, logout


class YoungSignUp(View):

    def post(self, request):
        data = request.POST

        print(data)
        try:
            user = User.objects.create_user(
                data['first_name'] + data['last_name'],
                data['email'],
                data['password'])
            profile = YoungProfile.objects.create(
                user=user,
                first_name=data['first_name'],
                last_names=data['last_name'],
                level=data['level'],
                interest_area=data['interest_area'],
                description=data['description']
            )

            logged_user = authenticate(username=user.username, password=data['password'])

            if not logged_user:
                raise User.DoesNotExist

        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, 'Ocurrio un error: ' + e)
            return redirect('young_signup')

        return redirect('services_list')


class LoginView(View):

    def post(self, request):
        data = request.POST

        try:
            user = User.objects.get(email=data['email'])
            logged_user = authenticate(username=user.username, password=data['password'])
            if not logged_user:
                raise User.DoesNotExist

        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, 'Correo o contraseña no valida')

        return redirect('services_list')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')
