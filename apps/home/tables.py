import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from . import models as home_models


class WarrantyFormTable(tables.Table):
    # email = tables.Column(empty_values=())
    # user_name = tables.Column(empty_values=(), verbose_name='Users')
    # interested_in_other_job_sectors = tables.Column(empty_values=())
    # sia_badge_for_security_guard = tables.Column(empty_values=(), verbose_name='SIA Badge')
    # driving_licence_for_driver = tables.Column(empty_values=(), verbose_name='Driving Licence')
    # legally_allowed_to_work_full_time = tables.Column(empty_values=(), verbose_name='Legally Allowed To Work')
    # created_at = tables.Column(empty_values=(), verbose_name='Register Date')

    # def render_driving_licence_for_driver(self, record):
    #     record: register_models.UserProfile
    #     if record.driving_licence_for_driver:
    #         return format_html(
    #             '<i style="color: green;display: flex; justify-content: center;" class="fas fa-check tick"></i>')
    #     return format_html(
    #         """<i style="color: red;display: flex; justify-content: center;" class="fas fa-times cross"></i>""")
    #
    # def render_interested_in_other_job_sectors(self, record):
    #     record: register_models.UserProfile
    #     if record.interested_in_other_job_sectors:
    #         return format_html(
    #             '<i style="color: green;display: flex; justify-content: center;" class="fas fa-check tick"></i>')
    #     return format_html(
    #         """<i style="color: red;display: flex; justify-content: center;" class="fas fa-times cross"></i>""")
    #
    # def render_legally_allowed_to_work_full_time(self, record):
    #     record: register_models.UserProfile
    #     if record.legally_allowed_to_work_full_time:
    #         return format_html(
    #             '<i style="color: green;display: flex; justify-content: center;" class="fas fa-check tick"></i>')
    #     return format_html(
    #         """<i style="color: red;display: flex; justify-content: center;" class="fas fa-times cross"></i>""")
    #
    # def render_sia_badge_for_security_guard(self, record):
    #     record: register_models.UserProfile
    #     if record.sia_badge_for_security_guard:
    #         return format_html(
    #             '<i style="color: green;display: flex; justify-content: center;" class="fas fa-check tick"></i>')
    #     return format_html(
    #         """<i style="color: red;display: flex; justify-content: center;" class="fas fa-times cross"></i>""")
    #
    # def render_email(self, record):
    #     record: register_models.UserProfile
    #     return record.user.email
    #
    # def render_created_at(self, record):
    #     record: register_models.UserProfile
    #     return record.created_at.date()
    #
    # def render_user_name(self, record, value):
    #     return format_html("""
    #      <a  href="{}">{}</a>
    #      """.format(reverse("add-comment-user", kwargs={"pk": record.user.pk}), record.user.get_full_name())
    # )

    class Meta:
        attrs = {"class": 'table table-sm  table-stripped data-table',
                 'data-add-url': 'Url here'}
        model = home_models.WarrantyForm
        fields = ['claim_number', 'Last_Name', 'First_Name', 'warranty_part', 'claim_submission_date',
                  'claim_approval_date', 'amount_submitted', 'has_claim_paid',
                  'claim_paid_date', 'status', 'amount_paid',
                  'submitted_by', 'notes', 'invoice_file', 'invoice_file_link']
