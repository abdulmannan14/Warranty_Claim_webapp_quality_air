# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, render

from . import models as home_models
from . import tables as home_tables
from . import forms as home_forms
from . import utils as home_utils
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url="/login/")
@csrf_exempt
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def my_forms(request):
    user_all_forms = home_models.WarrantyForm.objects.all()
    table = home_tables.WarrantyFormTable(user_all_forms)
    amount = home_utils.calculate_total_amount_of_this_year_forms(user_all_forms)
    context = {'segment': 'index',
               'table': table,
               'user_type': request.user.type,
               'submitted_amount': f'{amount.get("submitted_amount")}',
               'paid_amount': f'{amount.get("paid_amount")}',
               'non_paid_amount': f'{amount.get("non_paid_amount")}'

               }
    return render(request, 'home/table_view.html', context)


@login_required(login_url="/login/")
def add_new_warranty_forms(request):
    form = home_forms.WarrantyForm()
    if request.method == 'POST':
        form = home_forms.WarrantyForm(request.POST)
        obj = None
        if form.is_valid():
            obj = form.save()
        if request.FILES:
            obj.invoice_file = request.FILES['invoice_file']
        obj.user = request.user
        obj.save()
        # now send the email to the user who is logged in and submitted the form.
        home_utils.send_email_to_user(request.user, obj)
        messages.success(request, f'Form Submitted & Email sent to {obj.Last_Name} {obj.First_Name}')
        return redirect('my-forms')
        # return HttpResponseRedirect(reverse('my-forms'))

    context = {'segment': 'index',
               'form': form}
    return render(request, 'home/add_or_edit.html', context)


@login_required(login_url="/login/")
def export_all_forms(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    print("=================", start_date,
          end_date)
    response = home_utils.export_all_forms(start_date, end_date)
    # if not response[0]:
    #     messages.error(request, response[1])
    #     return redirect('my-forms')
    # else:
    return response


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
