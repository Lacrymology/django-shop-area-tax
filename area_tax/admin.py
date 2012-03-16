from django.contrib import admin
from area_tax.models import AreaTax

from l10n.admin import CountryAreaAdmin

class AreaTaxAdmin(CountryAreaAdmin):
    """
    Admin class for AreaTax. Constrains the data types
    """
    #exclude = ('content_type', 'object_id',)
admin.site.register(AreaTax, AreaTaxAdmin)
