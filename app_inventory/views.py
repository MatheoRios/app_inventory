from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseServerError
from django.template import loader
from app_inventory.models import mstr_catalog



def index(request):
    
    template = loader.get_template("index.html")
    return HttpResponse(template.render())




from django.shortcuts import render

def vw_catalogos(request):
    try:
        inv_catalago = mstr_catalog.objects.all().values()
        context = {'mymembers': inv_catalago}
        return render(request, 'index.html', context)
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")