from django.db import models
from uuid import uuid4
from accounts.models import UserModel


# Create your models here.
class LoanApplication(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    applicant_name = models.CharField(max_length=255)
    applicant_account = models.PositiveBigIntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    # collateral = models.FileField(upload_to='collaterals/')
    duration = models.CharField(max_length=10)
    account_officer = models.CharField(max_length=255)
    status = models.CharField(max_length=10, default="Pending")
    comment = models.TextField(default="")
    recipient = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date_applied = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.applicant_name


class LoanReview(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    official = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    applicant = models.ForeignKey(LoanApplication, related_name='approvals', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    comment = models.TextField()
    recipient = models.ForeignKey(UserModel, related_name='recipient', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.applicant.applicant_name
