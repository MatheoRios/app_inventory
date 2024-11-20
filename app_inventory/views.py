from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseServerError
from django.template import loader
from app_inventory.database_operations import query_all 
from app_inventory.models import states




def index(request):
    
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def vw_states(request):
    try:
        state = query_all(states)
        context = {'state': state}
        print(context)
        return render(request, 'index.html', context)
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")
    
    
