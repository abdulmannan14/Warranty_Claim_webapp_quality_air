from django.core.mail import send_mail
from django.conf import settings
from . import models as home_models
from django.db.models import Sum, Count
from django.db.models.functions import ExtractMonth
from datetime import datetime


def send_email_to_user(user, obj):
    subject = 'Thank you for submitting the warranty form'
    message = f' The warranty claim for {obj.Last_Name} {obj.First_Name} has been submitted.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)


def export_all_forms(start_date, end_date):
    from django.utils.dateparse import parse_date

    import csv
    from django.http import HttpResponse
    from .models import WarrantyForm
    # start_date = parse_date(start_date)
    # end_date = parse_date(end_date)
    if start_date and end_date and start_date <= end_date:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_forms.csv"'
        writer = csv.writer(response)
        writer.writerow(
            ['claim_number', 'Last_Name', 'First_Name', 'warranty_part', 'claim_submission_date', 'claim_approval_date',
             'amount_submitted', 'has_claim_paid', 'claim_paid_date', 'status', 'amount_paid', 'submitted_by', 'notes',
             'warranty_type'])
        all_forms = WarrantyForm.objects.filter(created_at__gte=start_date, created_at__lte=end_date)
        print("these are the forms", all_forms)
        for form in all_forms:
            writer.writerow(
                [form.claim_number, form.Last_Name, form.First_Name, form.warranty_part, form.claim_submission_date,
                 form.claim_approval_date, form.amount_submitted, form.has_claim_paid, form.claim_paid_date,
                 form.status,
                 form.amount_paid, form.submitted_by, form.notes, form.warranty_type])
        return response

    return False, "Invalid Date Range"


def calculate_total_amount_of_this_year_forms(user_all_forms):
    import datetime
    current_year = datetime.datetime.now().year
    submitted_amount = 0
    paid_amount = 0
    non_paid_amount = 0
    for form in user_all_forms:
        try:
            if form.claim_paid_date.year == current_year:
                submitted_amount += form.amount_submitted
                paid_amount += form.amount_paid
        except:
            pass
    non_paid_amount = submitted_amount - paid_amount
    return {"submitted_amount": f'${submitted_amount}', "paid_amount": f'${paid_amount}',
            "non_paid_amount": f'${non_paid_amount}'}


def calculate_monthly_amount_of_this_year_forms(forms):
    current_year = datetime.now().year
    monthly_amount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    monthly_amounts = (
        forms.filter(claim_paid_date__year=current_year)  # Filter for current year
        .annotate(month=ExtractMonth('claim_paid_date'))  # Extract the month from the created_at field
        .values('month')  # Group by month
        .annotate(total_amount=Sum('amount_paid'))  # Sum the amounts for each month
        .order_by('month')  # Order by month (optional)
    )
    for amount in monthly_amounts:
        monthly_amount[amount['month'] - 1] = (int(amount['total_amount'])) if amount['total_amount'] > 0 else 0
    return monthly_amount


def calculate_monthly_quantity_of_this_year_forms(forms):
    print("total form=====", forms.count())
    current_year = datetime.now().year
    monthly_quantity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    monthly_quantities = (
        forms.filter(claim_submission_date__year=current_year)  # Filter for current year
        .annotate(month=ExtractMonth('claim_submission_date'))  # Extract the month from the created_at field
        .values('month')  # Group by month
        .annotate(form_count=Count('id'))  # Sum the amounts for each month
        .order_by('month')  # Order by month (optional)
    )
    for quantity in monthly_quantities:
        monthly_quantity[quantity['month'] - 1] = quantity['form_count']
    return monthly_quantity
