# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
completed_paid_warrantly_claim = "COMPLETED/PAID WARRANTY CLAIM"
no_credit_received = "NO CREDIT RECEIVED"
claim_not_completed_or_paid = "CLAIM NOT COMPLETED or PAID"
shipping_not_paid_in_claim = "SHIPPING NOT PAID IN CLAIM"
no_invoice_for_part = "NO INVOICE FOR PART = NO CREDIT"
requires_distributor_review = "REQUIRES DISTRIBUTOR REVIEW"
repair_exceeds_normal_limits = " REPAIR EXCEEDS NORMAL LIMITS"
waiting_on_chad = "WAITING ON CHAD"

status_choices = [(completed_paid_warrantly_claim, completed_paid_warrantly_claim),
                  (no_credit_received, no_credit_received),
                  (claim_not_completed_or_paid, claim_not_completed_or_paid),
                  (shipping_not_paid_in_claim, shipping_not_paid_in_claim),
                  (no_invoice_for_part, no_invoice_for_part),
                  (requires_distributor_review, requires_distributor_review),
                  (repair_exceeds_normal_limits, repair_exceeds_normal_limits),
                  (waiting_on_chad, waiting_on_chad)
                  ]

carrier = "Carrier"
ferguson = "Ferguson"
goodman = "Goodman"
honeywell = "Honeywell"
lennox = "Lennox"
mitsubishi = "Mitsubishi"
trane = "Trane"
quality_air = "Quality Air"
warranty_type_choices = [(carrier, carrier), (ferguson, ferguson), (goodman, goodman), (honeywell, honeywell),
                         (lennox, lennox), (mitsubishi, mitsubishi), (trane, trane), (quality_air, quality_air)]


class WarrantyForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    claim_number = models.CharField(max_length=100, null=True, blank=True)
    Last_Name = models.CharField(max_length=100, null=True, blank=True)
    First_Name = models.CharField(max_length=100, null=True, blank=True)
    warranty_part = models.CharField(max_length=100, null=True, blank=True)
    claim_submission_date = models.DateField(null=True, blank=True)
    claim_approval_date = models.DateField(null=True, blank=True)
    amount_submitted = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    has_claim_paid = models.BooleanField(default=False, null=True, blank=True)
    claim_paid_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choices, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    submitted_by = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    invoice_file = models.FileField(upload_to='invoices/', null=True, blank=True)
    warranty_type = models.CharField(max_length=100, choices=warranty_type_choices, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    creation_time = models.DateField(auto_now_add=True)
    # invoice_file_link = models.CharField(max_length=100, null=True, blank=True)
