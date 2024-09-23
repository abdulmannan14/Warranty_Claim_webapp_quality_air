from apps.authentication import forms
from . import models as home_models
from django import forms


class WarrantyForm(forms.ModelForm):
    # define rows and columns for the text area
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}), required=False)
    claim_submission_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    claim_approval_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    claim_paid_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = home_models.WarrantyForm
        fields = ['claim_number', 'Last_Name', 'First_Name', 'warranty_part', 'amount_paid', 'amount_submitted',
                  'claim_submission_date',
                  'claim_approval_date', 'claim_paid_date',
                  'submitted_by', 'has_claim_paid', 'status', 'warranty_type', 'invoice_file', 'notes']
