from django.core.mail import send_mail
from django.conf import settings


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
