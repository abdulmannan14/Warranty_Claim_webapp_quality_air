# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from . import models as home_models
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Step 1: Define a resource class for the model
class WarrantFormResource(resources.ModelResource):
    class Meta:
        model = home_models.WarrantyForm  # The model you're adding import/export for
        # You can specify fields to include/exclude during import/export
        fields = ('id', 'claim_number', 'Last_Name', 'First_Name', 'warranty_part', 'claim_submission_date',
                  'claim_approval_date', 'amount_submitted', 'claim_paid_date',
                  'amount_paid', 'submitted_by', 'notes',)
        # You can also exclude fields by using the `exclude` option
        # exclude = ('id',)


# Step 2: Create the Admin class
class WarrantFormAdmin(ImportExportModelAdmin):
    resource_class = WarrantFormResource
    search_help_text = None

    # Other admin customizations can be added here as needed


# Step 3: Register the Admin class with the model
admin.site.register(home_models.WarrantyForm, WarrantFormAdmin)
