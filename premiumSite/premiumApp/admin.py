from django.contrib import admin
from .models import PremiumModel, FinanceModel, TemporaryModel

# Register your models here.
admin.site.register(PremiumModel)
admin.site.register(FinanceModel)
admin.site.register(TemporaryModel)