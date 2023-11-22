from django.contrib import admin
from store.models import Product,Variation

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','slug','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}
# Register your models here.
admin.site.register(Product,ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active')
    list_editable = ('is_active',)
# Register your models here.

admin.site.register(Variation,VariationAdmin)