from django.db import models
from .choices import gender, type

# Create your models here.

class countries(models.Model):
    count_name = models.CharField(("Country Name"), max_length=50)
    count_iso3 = models.CharField(("Country ISO3"), max_length=3)
    count_iso2 = models.CharField(("Country ISO2"), max_length=3)
    count_phone = models.CharField(("Country Phone Code"), max_length=5,null=True)
    count_currency = models.CharField(("Country Currency"), max_length=3,null=True)
    count_tld = models.CharField(("Country TLD"), max_length=5)

    class Meta:
        db_table = ('countries')
        verbose_name = ("country")
        verbose_name_plural = ("countries")

    def __str__(self):
        return self.count_name

class states(models.Model):
    state_name = models.CharField(("State Name"), max_length=100,blank=True)
    count = models.ForeignKey(countries, verbose_name=(""), on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = ('states')
        verbose_name = ("state")
        verbose_name_plural = ("states")

    def __str__(self):
        return self.state_name
    
class cities(models.Model):
    city_name = models.CharField(("State Name"), max_length=100)
    state = models.ForeignKey(states, verbose_name=(""), on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = ('cities')
        verbose_name = ("city")
        verbose_name_plural = ("cities")

    def __str__(self):
        return self.city_name

class mstr_subcatalog(models.Model):
    subca_code = models.CharField(("subcatalog Code"), max_length=25,null=True)
    subca_descr = models.CharField(("subcatalog Description"), max_length=25,null=True)

    class Meta:
        db_table =('mstr_subcatalog')
        verbose_name = ("subcatalog")
        verbose_name_plural = ("subcatalogs")

    def __str__(self):
        return self.subca_descr

class mstr_size(models.Model):
    size_code = models.CharField(("Size Code"), max_length=25)
    size_descr = models.CharField(("Size Description"), max_length=25)

    class Meta:
        db_table =('mstr_size')
        verbose_name =("Size")
        verbose_name_plural =("Sizes")

    def __str__(self):
        return self.size_descr

class mstr_model(models.Model):
    model_code = models.CharField(("Model Code"), max_length=25)
    model_descr = models.CharField(("Model Description"), max_length=25)

    class Meta:
        db_table =('mstr_model')
        verbose_name =("Model")
        verbose_name_plural =("Models")

    def __str__(self):
        return self.model_descr

class mstr_color(models.Model):
    color_code = models.CharField(("Color Code"), max_length=25,null=True)
    color_name = models.CharField(("Color Description"), max_length=25)

    class Meta:
        db_table =('mstr_color')
        verbose_name =("color")
        verbose_name_plural =("colors")

    def __str__(self):
        return self.color_name

class mstr_catalog(models.Model):
    catal_code = models.CharField(("Catalog Code"), max_length=25,null=True)
    catal_descr = models.CharField(("Catalog Description"), max_length=25)

    class Meta:
        db_table =('mstr_catalog')
        verbose_name =("Catalog")
        verbose_name_plural =("Catalogs")

    def __str__(self):
        return self.catal_descr
    
class warehousedb(models.Model):
    wareh_cod = models.CharField(("Warehouse Code"), max_length=25)
    wareh_name = models.CharField(("Warehouse Name"), max_length=50)

    class Meta:
        db_table =('warehouse')
        verbose_name =("warehouse")
        verbose_name_plural =("warehouses")

    def __str__(self):
        return self.wareh_name

class suppliersdb(models.Model):
    suppl_tax_name = models.TextField(("Supplier Tax Name"))
    suppl_short_name = models.CharField(("Supplier Short Name"), max_length=25)
    suppl_addre = models.TextField(("Supplier Address"))
    suppl_ident = models.CharField(("Supplier nro. Identification"), max_length=20)
    state = models.ForeignKey(states, verbose_name=(""), on_delete=models.CASCADE)
    city = models.ForeignKey(cities, verbose_name=(""), on_delete=models.CASCADE)
    suppl_contac = models.CharField(("Supplier Contact"), max_length=25)
    suppl_email = models.CharField(("Supplier Contact"), max_length=50)
    suppl_phone = models.CharField(("Supplier Phone"), max_length=50)

    class Meta:
        db_table =('suppliers')
        verbose_name =("supplie")
        verbose_name_plural =("suppliers")

    def __str__(self):
        return self.suppl_short_name

class salesdb(models.Model):
    produ_cod = models.IntegerField(verbose_name='Master code')
    sales_qty = models.IntegerField(("Sales Quantity "))
    sales_date = models.DateTimeField(("Date Sales"), auto_now_add=False)

    class Meta:
        db_table =('sales')
        verbose_name =("sale")
        verbose_name_plural =("sales")

    # def __str__(self):
    #     return self.name

class departmentsdb(models.Model):
    depar_cod = models.CharField(("Departament Code"), max_length=25)
    depar_name = models.CharField(("Departament Name"), max_length=50)

    class Meta:
        db_table =('departments')
        verbose_name =("department")
        verbose_name_plural =("departments")

    def __str__(self):
        return self.depar_name
    
class productsdb(models.Model):
    suppl = models.ForeignKey(suppliersdb, verbose_name=(""), on_delete=models.CASCADE)
    produ_cod = models.IntegerField(verbose_name='Master code')
    produ_qr = models.IntegerField(verbose_name='QR code')
    produ_title = models.CharField(("Title"), max_length=25)
    produ_descr_gral = models.CharField(("Description"), max_length=50)
    depar = models.ForeignKey(departmentsdb, verbose_name=(""), on_delete=models.CASCADE)
    catal = models.ForeignKey(mstr_catalog, verbose_name=(""), on_delete=models.CASCADE)
    subca = models.ForeignKey(mstr_subcatalog, verbose_name=(""), on_delete=models.CASCADE)
    model = models.ForeignKey(mstr_model, verbose_name=(""), on_delete=models.CASCADE)
    color = models.ForeignKey(mstr_color, verbose_name=(""), on_delete=models.CASCADE)
    size = models.ForeignKey(mstr_size, verbose_name=(""), on_delete=models.CASCADE)
    gender = models.CharField(("Gender"),max_length=1, choices=gender, default='O')
    produ_regis_date = models.DateTimeField(("Date Register"), auto_now_add=True)
    produ_active = models.BooleanField(("Active"))  

    class Meta:
        db_table =('products')
        verbose_name =("product")
        verbose_name_plural =("products")

    def __str__(self):
        return self.produ_descr_gral

class ordersdb(models.Model):
    order_cod = models.CharField((""), max_length=25)
    order_type = models.SmallIntegerField(("Order Type"))
    produ = models.ForeignKey(productsdb, verbose_name=(""), on_delete=models.RESTRICT)
    sales_user = models.SmallIntegerField(("Sales User"))
    sales_qty = models.IntegerField(("Sales Quantity "))
    wareh_user = models.SmallIntegerField(("Warehouse User"))
    wareh_qty = models.IntegerField(("Quantity Warehouse"))
    picki_user = models.SmallIntegerField(("Picking User"))
    picki_qty = models.IntegerField(("Picking Quantity"))
    order_date = models.DateTimeField(("Date Order"), auto_now_add=True)
    order_status = models.SmallIntegerField(("Order Status"))

    class Meta:
        db_table =('orders')
        verbose_name =("order")
        verbose_name_plural =("orders")

    def __str__(self):
        return self.order_cod

class wh_locationsdb(models.Model):
    wareh = models.ForeignKey(warehousedb, verbose_name=(""), on_delete=models.CASCADE)
    wh_locat_code = models.CharField(("Warehouse Locations Code"), max_length=25)
    wh_locat_name = models.CharField(("Warehouse Locations Name"), max_length=25)

    class Meta:
        db_table =('wh_locations')
        verbose_name =("Location")
        verbose_name_plural =("Locations")

    def __str__(self):
        return self.wh_locat_name
    
class inventorydb(models.Model):
    wareh = models.ForeignKey(warehousedb, verbose_name=(""), on_delete=models.CASCADE)
    produ = models.ForeignKey(productsdb, verbose_name=(""), on_delete=models.CASCADE)
    type = models.IntegerField(("Transaction Type"), choices=type, default=1)
    qty = models.IntegerField(("Quantity"))

    class Meta:
        db_table =('inventory')
        verbose_name =("inventory")
        verbose_name_plural =("inventories")
    