from django.contrib import admin
from store.models import Product, Variation

# Register your models here.
class ProductAdmin(admin.ModelAdmin): 
    prepopulated_fields = {'slug' : ('product_name',)} 
    list_display = ('product_name', 'slug', 'price', 'stock', 'category', 'modified_date', 'is_available') 
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active') 
    list_editable = ('is_active',)
     
admin.site.register(Product,ProductAdmin) 
admin.site.register(Variation,VariationAdmin) 
 