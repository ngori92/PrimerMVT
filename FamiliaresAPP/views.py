from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from FamiliaresAPP.models import Familiar

# Create your views here.
def familiares(request):
    misFamiliares = Familiar.objects.all().values()
    template = loader.get_template("template1.html")
    context = {
        "misFamiliares": misFamiliares
    }
    
    return HttpResponse(template.render(context, request))