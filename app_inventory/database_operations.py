
#Funcion que se encarga de retornar todas las ciudades


def query_all(objecto):
    
     try:
        get_objects = objecto.objects.all().values()
        return get_objects
     except Exception as e:
          raise e



     
     

     # end try
     
     

     
          
     
          