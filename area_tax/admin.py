from django.contrib import admin
from area_tax.models import AreaTax

class AreaTaxAdmin(admin.ModelAdmin):
    """
    Admin class for AreaTax. Constrains the data types
    """
    exclude = ('content_type', 'object_id',)
admin.site.register(AreaTax, AreaTaxAdmin)
