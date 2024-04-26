# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:14:46 2024

@author: EXU552
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('select_environment/', views.select_environment, name='select_environment'),
    path('open_svg/', views.open_svg, name='open_svg'),
]