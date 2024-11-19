from django.db import models

# Create your models here.

class mstr_models(models.Model):
    models_id = models.CharField("models_id",max_length=50)
    models_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.models_desc 
    
class mstr_color(models.Model):

    color_cod = models.CharField("codigo color alfanuemrico",max_length=50)
    color_name = models.CharField(max_length=200)


    def __str__(self):
        return self.color_name
    
     
class mstr_sizes(models.Model):

    size_cod = models.CharField("Codigo de la talla", max_length=20)
    size_desc = models.CharField("Descripcion de la talla")
    
    def __str__(self):
        return self.size_desc
    
class mstr_catalog(models.Model):

     catal_cod = models.CharField("codigo  alfanumerico",max_length=20)
     catal_descr = models.CharField("Descripcion del catalago")

     def __str__(self):
        return self.catal_descr
    
     
class mstr_subcatalog(models.Model):

    subcatal_cod = models.CharField("El codigo alfanumerico de catalago")
    subcatal_descr = models.CharField("descrpcion de catalago")
    
    def __str__(self):
        return self.subcatal_descr
    
class departaments(models.Model):

    depar_cod = models.CharField("codigo alfamumerico del departamento",max_length=20)
    depar_descr = models.CharField("Descripcion del departamento",max_length=200)

    def __str__(self):
        return self.depar_descr

class countries(models.Model):

    count_name = models.CharField("nombre del pais", max_length=100)
    count_iso3 = models.CharField("count_iso3",max_length=100)
    count_iso2 = models.CharField("count_iso2",max_length=100)
    count_phone_code = models.CharField("codigo de telefono del pais",max_length=20)
    count_concurrencia = models.CharField("count_concurrencia",max_length=50)
    count_tld= models.CharField("count_tld",max_length=100)
    
    def __str__(self):
        return self.count_name
  
  
class states(models.Model):
    state_id = models.CharField("id de la ciudad",max_length=100)
    states_name = models.CharField("nombre del estado",max_length=100)
 
    
    def __str__(self):
        return self.states_name
 
 
class cities(models.Model):
 
    city_name = models.CharField("nombre de la ciudad",max_length=100)
    states_id = models.ForeignKey(states, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.city_name
 

class suppliers(models.Model):
    
    suppl_tax_name = models.CharField("",max_length=100)
    suppl_short_name = models.CharField("nombre corto",max_length=100)
    suppl_address = models.CharField("direccion proveedor",max_length=200)
    suppl_nr_identif = models.CharField("rif proveedor",max_length=200)
    count_id = models.IntegerField()
    states_id = models.ForeignKey(states, on_delete=models.CASCADE) 
    city_id = models.ForeignKey(cities, on_delete=models.CASCADE) 
    suppl_contact = models.CharField("",max_length=100)
    suppl_email = models.EmailField(("correo electronico"), max_length=200)
    suppl_phone = models.CharField()
    
    def __str__(self):
        return self.suppl_tax_name
  
    

class products(models.Model):
        produ_id = models.IntegerField(("id del producto de tipo  varchar"))
        #relacion proveedor id
        suppl_id = models.ForeignKey(suppliers, on_delete=models.CASCADE)
        produ_cod = models.CharField("codigo del producto", max_length=50)
        produc_qr = models.CharField("codigo para generar el codigo QR", max_length=50)
        produ_title = models.CharField("titulo  del producto", max_length=200)
        produ_descrip_gral = models.CharField(("Descripcion general del prodcuto"), max_length=200)
        #relacion departamento id
        depa_id = models.ForeignKey(departaments, on_delete=models.CASCADE) 
        #relacion subcatalago id
        cata_id =  models.ForeignKey(mstr_catalog, on_delete=models.CASCADE) 
        #relacion subcatalago id
        subcatal_id = models.ForeignKey(mstr_subcatalog, on_delete=models.CASCADE) 
         #relacion modelo id
        models_id = models.ForeignKey(mstr_models, on_delete=models.CASCADE)
        #relacion color id
        color_id = models.ForeignKey(mstr_color, on_delete=models.CASCADE) 

        gender = models.CharField(max_length=100) 
        
        produ_regis_date = models.DateField()
        
        produ_active = models.BooleanField(default=True)

        def __str__(self):
            return  str(self.produ_id) + " " + self.produ_descrip_gral + " " +  self.produ_cod + " " + str(self.produ_active)


class sales(models.Model):
    
     produ_cod = models.CharField("codigo del producto",max_length=20)
     sales_qty = models.DecimalField(max_digits=18, decimal_places=4)
     sale_datatime = models.DateTimeField()

     def __init__(self):
        return self.sale_id
    
class orders(models.Model):
    
    orde_cod = models.ForeignKey(sales, on_delete=models.CASCADE) 
    order_type =  models.CharField(max_length=50)
    produc_id = models.CharField("codigo del producto",max_length=100)
    sales_qty =models.DecimalField(max_digits=18, decimal_places=4)
    repos_qty = models.DecimalField(max_digits=18, decimal_places=4)
    picki_qty = models.DecimalField(max_digits=18, decimal_places=4)
    order_datetime = models.DateTimeField()
    order_status = models.BooleanField()
    sales_user = models.CharField("nombre del usaurio",max_length=30)
    wh1_user =  models.CharField(max_length=30)
    pick_user = models.CharField("nombre del usaurio",max_length=30)
    
    def __init__(self):
        return self.order_id
    
    
class warehouse(models.Model):
        
    ware_cod = models.CharField("codido deposito",max_length=30)
    ware_descr= models.CharField("descripcion del deposito",max_length=30)

    def __init__(self):
        
        return self.ware_descr
    
class warehouse_location(models.Model):
    
    wareh_id = models.ForeignKey(warehouse, on_delete=models.CASCADE) 
    locat_code = models.CharField(max_length=30)
    locat_descr = models.CharField("descripcion location", max_length=100)

    
class inventory(models.Model):
    wareh_id = models.ForeignKey(warehouse, on_delete=models.CASCADE) 
    produ_id = models.ForeignKey(products, on_delete=models.CASCADE) 
    locat_id = models.ForeignKey(warehouse_location, on_delete=models.CASCADE) 
    
    def __init__(self):
        return self.inven_id
