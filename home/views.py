# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class HomeView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('services_list')
        return render(request, "home/index.html")
