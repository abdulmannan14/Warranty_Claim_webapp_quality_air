import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from . import models as home_models


class WarrantyFormTable(tables.Table):
    invoice_file = tables.Column(empty_values=(), orderable=False)

    class Meta:
        attrs = {"class": 'table table-sm  table-stripped data-table',
                 'data-add-url': 'Url here'}
        model = home_models.WarrantyForm
        fields = ['claim_number', 'Last_Name', 'First_Name', 'warranty_part', 'claim_submission_date',
                  'claim_approval_date', 'amount_submitted', 'has_claim_paid',
                  'claim_paid_date', 'status', 'amount_paid',
                  'submitted_by', 'notes', 'invoice_file']

    def render_invoice_file(self, record):
        try:
            #     when we click on url it should open on target blank
            return format_html('<a href="{}" target="_blank">View Invoice</a>',
                               record.invoice_file.url)
        except:
            pass
