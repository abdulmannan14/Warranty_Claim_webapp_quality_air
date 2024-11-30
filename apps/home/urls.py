# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('warranty_forms', views.my_forms, name='my-forms'),
    path('add_new_warranty_form', views.add_new_warranty_forms, name='add-new-warranty-form'),
    path('export_all_forms', views.export_all_forms, name='export-all-forms'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
