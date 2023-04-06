from django.shortcuts import render, HttpResponse
from .models import PremiumModel, FinanceModel, TemporaryModel


# Create your views here.
def home(request):
    data = FinanceModel.objects.all()
    context = {
        'data':data
    }
    return render(request, "premiumApp/claims.html", context)