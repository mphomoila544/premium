from django.db import models

# Create your models here.
class PremiumModel(models.Model):
    scheme_name = models.CharField(max_length=200)
    insurer_name = models.CharField(max_length=200)
    consultant_name = models.CharField(max_length=300, default="null", null = True)
    policy_number = models.CharField(max_length=20, unique=True)
    active = "active"
    inactive = "inactive"
    scheme_status_choices = [
        (active, "active"),
        (inactive, "inactive")
    ]
    scheme_status = models.CharField(max_length=20, choices=scheme_status_choices)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)

    cancelled = "cancelled"
    lapsed = "lapsed"
    policy_status_choices = [
        (active, "active"),
        (inactive, "inactive"),
        (lapsed, "lapsed"),
        (cancelled, "cancelled")
    ]
    policy_status = models.CharField(max_length=20, choices=policy_status_choices)
    gross_premium = models.FloatField(null=True)

    """gross_premium = models.FloatField(null=True)
    srs_risk_premium = models.FloatField(null=True)
    arl_risk_premium = models.FloatField(null=True)
    premium_increase_factor = models.FloatField(null = True)
    safrican_risk_before_increase = models.FloatField(null=True)
    srs_claims_binder_fee = models.FloatField(null=True)
    net_insurer_prem = models.FloatField(null=True)
    srs_admin_fee = models.FloatField(null = True)
    total_srs_fee = models.FloatField(null=True)"""


class TemporaryModel(models.Model):
    scheme_names = models.CharField(max_length=200)

class FinanceModel(models.Model):
    policy_number = models.ForeignKey(PremiumModel,to_field='policy_number', on_delete=models.CASCADE)
    srs_risk_premium = models.FloatField(null=True)
    invoice_amount = models.FloatField(null=True)
    proof_of_payment = models.FileField(upload_to='proofOfPayment', null=True)
    
    def __str__(self):
        return self.policy_number

