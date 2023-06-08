from django.contrib import admin
from .models import LoanApplication, LoanReview


# Register your models here.
@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ("applicant_name", "applicant_account", "date_applied")
    list_filter = ("status", "date_applied")


@admin.register(LoanReview)
class LoanReviewAdmin(admin.ModelAdmin):
    list_display = ("official", "applicant", "status", "comment")
    list_filter = ("status",)
