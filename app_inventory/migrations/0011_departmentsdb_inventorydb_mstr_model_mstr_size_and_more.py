# Generated by Django 4.2.16 on 2024-11-20 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventory', '0010_remove_cities_countr_id_states_countr_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='departmentsdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depar_cod', models.CharField(max_length=25, verbose_name='Departament Code')),
                ('depar_name', models.CharField(max_length=50, verbose_name='Departament Name')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='inventorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[('0', 'Egreso'), ('1', 'Ingreso')], default=1, verbose_name='Transaction Type')),
                ('qty', models.IntegerField(verbose_name='Quantity')),
            ],
            options={
                'verbose_name': 'inventory',
                'verbose_name_plural': 'inventories',
                'db_table': 'inventory',
            },
        ),
        migrations.CreateModel(
            name='mstr_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_code', models.CharField(max_length=25, verbose_name='Model Code')),
                ('model_descr', models.CharField(max_length=25, verbose_name='Model Description')),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
                'db_table': 'mstr_model',
            },
        ),
        migrations.CreateModel(
            name='mstr_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_code', models.CharField(max_length=25, verbose_name='Size Code')),
                ('size_descr', models.CharField(max_length=25, verbose_name='Size Description')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
                'db_table': 'mstr_size',
            },
        ),
        migrations.CreateModel(
            name='ordersdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_cod', models.CharField(max_length=25, verbose_name='')),
                ('order_type', models.SmallIntegerField(verbose_name='Order Type')),
                ('sales_user', models.SmallIntegerField(verbose_name='Sales User')),
                ('sales_qty', models.IntegerField(verbose_name='Sales Quantity ')),
                ('wareh_user', models.SmallIntegerField(verbose_name='Warehouse User')),
                ('wareh_qty', models.IntegerField(verbose_name='Quantity Warehouse')),
                ('picki_user', models.SmallIntegerField(verbose_name='Picking User')),
                ('picki_qty', models.IntegerField(verbose_name='Picking Quantity')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Order')),
                ('order_status', models.SmallIntegerField(verbose_name='Order Status')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='productsdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produ_cod', models.IntegerField(verbose_name='Master code')),
                ('produ_qr', models.IntegerField(verbose_name='QR code')),
                ('produ_title', models.CharField(max_length=25, verbose_name='Title')),
                ('produ_descr_gral', models.CharField(max_length=50, verbose_name='Description')),
                ('gender', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otros')], default='O', max_length=1, verbose_name='Gender')),
                ('produ_regis_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Register')),
                ('produ_active', models.BooleanField(verbose_name='Active')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='salesdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produ_cod', models.IntegerField(verbose_name='Master code')),
                ('sales_qty', models.IntegerField(verbose_name='Sales Quantity ')),
                ('sales_date', models.DateTimeField(verbose_name='Date Sales')),
            ],
            options={
                'verbose_name': 'sale',
                'verbose_name_plural': 'sales',
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='suppliersdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppl_tax_name', models.TextField(verbose_name='Supplier Tax Name')),
                ('suppl_short_name', models.CharField(max_length=25, verbose_name='Supplier Short Name')),
                ('suppl_addre', models.TextField(verbose_name='Supplier Address')),
                ('suppl_ident', models.CharField(max_length=20, verbose_name='Supplier nro. Identification')),
                ('suppl_contac', models.CharField(max_length=25, verbose_name='Supplier Contact')),
                ('suppl_email', models.CharField(max_length=50, verbose_name='Supplier Contact')),
                ('suppl_phone', models.CharField(max_length=50, verbose_name='Supplier Phone')),
            ],
            options={
                'verbose_name': 'supplie',
                'verbose_name_plural': 'suppliers',
                'db_table': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='warehousedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wareh_cod', models.CharField(max_length=25, verbose_name='Warehouse Code')),
                ('wareh_name', models.CharField(max_length=50, verbose_name='Warehouse Name')),
            ],
            options={
                'verbose_name': 'warehouse',
                'verbose_name_plural': 'warehouses',
                'db_table': 'warehouse',
            },
        ),
        migrations.CreateModel(
            name='wh_locationsdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wh_locat_code', models.CharField(max_length=25, verbose_name='Warehouse Locations Code')),
                ('wh_locat_name', models.CharField(max_length=25, verbose_name='Warehouse Locations Name')),
                ('wareh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.warehousedb', verbose_name='')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
                'db_table': 'wh_locations',
            },
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='locat_id',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='produ_id',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='wareh_id',
        ),
        migrations.DeleteModel(
            name='mstr_sizes',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='orde_cod',
        ),
        migrations.RemoveField(
            model_name='products',
            name='cata_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='color_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='depa_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='models_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='subcatal_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='suppl_id',
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='states_id',
        ),
        migrations.RemoveField(
            model_name='warehouse_location',
            name='wareh_id',
        ),
        migrations.AlterModelOptions(
            name='cities',
            options={'verbose_name': 'city', 'verbose_name_plural': 'cities'},
        ),
        migrations.AlterModelOptions(
            name='countries',
            options={'verbose_name': 'country', 'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelOptions(
            name='mstr_catalog',
            options={'verbose_name': 'Catalog', 'verbose_name_plural': 'Catalogs'},
        ),
        migrations.AlterModelOptions(
            name='mstr_color',
            options={'verbose_name': 'color', 'verbose_name_plural': 'colors'},
        ),
        migrations.AlterModelOptions(
            name='mstr_subcatalog',
            options={'verbose_name': 'subcatalog', 'verbose_name_plural': 'subcatalogs'},
        ),
        migrations.AlterModelOptions(
            name='states',
            options={'verbose_name': 'state', 'verbose_name_plural': 'states'},
        ),
        migrations.RemoveField(
            model_name='cities',
            name='states_id',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='count_concurrencia',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='count_phone_code',
        ),
        migrations.RemoveField(
            model_name='mstr_catalog',
            name='catal_cod',
        ),
        migrations.RemoveField(
            model_name='mstr_color',
            name='color_cod',
        ),
        migrations.RemoveField(
            model_name='mstr_subcatalog',
            name='subcatal_cod',
        ),
        migrations.RemoveField(
            model_name='mstr_subcatalog',
            name='subcatal_descr',
        ),
        migrations.RemoveField(
            model_name='states',
            name='countr_id',
        ),
        migrations.RemoveField(
            model_name='states',
            name='state_id',
        ),
        migrations.RemoveField(
            model_name='states',
            name='states_name',
        ),
        migrations.AddField(
            model_name='cities',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_inventory.states', verbose_name=''),
        ),
        migrations.AddField(
            model_name='countries',
            name='count_currency',
            field=models.CharField(max_length=3, null=True, verbose_name='Country Currency'),
        ),
        migrations.AddField(
            model_name='countries',
            name='count_phone',
            field=models.CharField(max_length=5, null=True, verbose_name='Country Phone Code'),
        ),
        migrations.AddField(
            model_name='mstr_catalog',
            name='catal_code',
            field=models.CharField(max_length=25, null=True, verbose_name='Catalog Code'),
        ),
        migrations.AddField(
            model_name='mstr_color',
            name='color_code',
            field=models.CharField(max_length=25, null=True, verbose_name='Color Code'),
        ),
        migrations.AddField(
            model_name='mstr_subcatalog',
            name='subca_code',
            field=models.CharField(max_length=25, null=True, verbose_name='subcatalog Code'),
        ),
        migrations.AddField(
            model_name='mstr_subcatalog',
            name='subca_descr',
            field=models.CharField(max_length=25, null=True, verbose_name='subcatalog Description'),
        ),
        migrations.AddField(
            model_name='states',
            name='count',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_inventory.countries', verbose_name=''),
        ),
        migrations.AddField(
            model_name='states',
            name='state_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='State Name'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='city_name',
            field=models.CharField(max_length=100, verbose_name='State Name'),
        ),
        migrations.AlterField(
            model_name='countries',
            name='count_iso2',
            field=models.CharField(max_length=3, verbose_name='Country ISO2'),
        ),
        migrations.AlterField(
            model_name='countries',
            name='count_iso3',
            field=models.CharField(max_length=3, verbose_name='Country ISO3'),
        ),
        migrations.AlterField(
            model_name='countries',
            name='count_name',
            field=models.CharField(max_length=50, verbose_name='Country Name'),
        ),
        migrations.AlterField(
            model_name='countries',
            name='count_tld',
            field=models.CharField(max_length=5, verbose_name='Country TLD'),
        ),
        migrations.AlterField(
            model_name='mstr_catalog',
            name='catal_descr',
            field=models.CharField(max_length=25, verbose_name='Catalog Description'),
        ),
        migrations.AlterField(
            model_name='mstr_color',
            name='color_name',
            field=models.CharField(max_length=25, verbose_name='Color Description'),
        ),
        migrations.AlterModelTable(
            name='cities',
            table='cities',
        ),
        migrations.AlterModelTable(
            name='countries',
            table='countries',
        ),
        migrations.AlterModelTable(
            name='mstr_catalog',
            table='mstr_catalog',
        ),
        migrations.AlterModelTable(
            name='mstr_color',
            table='mstr_color',
        ),
        migrations.AlterModelTable(
            name='mstr_subcatalog',
            table='mstr_subcatalog',
        ),
        migrations.AlterModelTable(
            name='states',
            table='states',
        ),
        migrations.DeleteModel(
            name='departaments',
        ),
        migrations.DeleteModel(
            name='inventory',
        ),
        migrations.DeleteModel(
            name='mstr_models',
        ),
        migrations.DeleteModel(
            name='orders',
        ),
        migrations.DeleteModel(
            name='products',
        ),
        migrations.DeleteModel(
            name='sales',
        ),
        migrations.DeleteModel(
            name='suppliers',
        ),
        migrations.DeleteModel(
            name='warehouse',
        ),
        migrations.DeleteModel(
            name='warehouse_location',
        ),
        migrations.AddField(
            model_name='suppliersdb',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.cities', verbose_name=''),
        ),
        migrations.AddField(
            model_name='suppliersdb',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.states', verbose_name=''),
        ),
        migrations.AddField(
            model_name='productsdb',
            name='catal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.mstr_catalog', verbose_name=''),
        ),
        migrations.AddField(
            model_name='productsdb',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.mstr_color', verbose_name=''),
        ),
        migrations.AddField(
            model_name='productsdb',
            name='depar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.departmentsdb', verbose_name=''),
        ),
        migrations.AddField(
            model_name='productsdb',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.mstr_model', verbose_name=''),
        ),
        migrations.AddField(
            model_name='productsdb',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.mstr_size', verbose_name=''),
        ),
        migrations.AddField(
            model_name='productsdb',
            name='subca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.mstr_subcatalog', verbose_name=''),
        ),
        migrations.AddField(
            model_name='productsdb',
            name='suppl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.suppliersdb', verbose_name=''),
        ),
        migrations.AddField(
            model_name='ordersdb',
            name='produ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app_inventory.productsdb', verbose_name=''),
        ),
        migrations.AddField(
            model_name='inventorydb',
            name='produ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.productsdb', verbose_name=''),
        ),
        migrations.AddField(
            model_name='inventorydb',
            name='wareh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventory.warehousedb', verbose_name=''),
        ),
    ]