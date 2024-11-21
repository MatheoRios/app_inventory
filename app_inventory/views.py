from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseServerError
from django.template import loader
from django.core.paginator import Paginator
from app_inventory.models import states,departmentsdb
from django.shortcuts import render, redirect 
from .forms import  DepartForm



def index(request):
    
    template = loader.get_template("layout.html")
    return HttpResponse(template.render())


# vista departamento muestra todos lo datos de la tabla    
def vw_departments(request):
    try:
        depart = departmentsdb.objects.all().order_by('id')
  # Ordenamos por fecha de creación
        paginator = Paginator(depart, 10)  # 10 posts por página
        page_number = request.GET.get('page')
        page_obj_depart = paginator.get_page(page_number)
   
        return render(request, 'departments.html', {'page_obj_depart': page_obj_depart})
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")
    
 # vista departamento muestra todos lo datos de la tabla      
    

 # vista departamento registra los departamentos    
def register_department(request):
    if request.method == 'POST':
        form = DepartForm(request.POST)
        if form.is_valid():
            form.save()
        
            return redirect('success_view')  # Redirect to success view
        else:
            return render(request, '404.html')
    else:
        form = DepartForm()
    return render(request, 'departments.html', {'form': form})
def success_view(request): 
     return render(request, 'success.html')
  # vista departamento registra los departamentos    
  

def edit_department(request, id):
    try:
        return HttpResponse(f"Si funciona la vista con ID: {id}")
    except Exception as e:
        raise e
    