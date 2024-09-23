# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from . import models as home_models

admin.site.register(home_models.WarrantyForm)
