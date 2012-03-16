from django.contrib import admin
from area_tax.models import AreaTax

from l10n.admin import CountryAreaAdmin

class AreaTaxAdmin(CountryAreaAdmin):
    """
    Admin class for AreaTax. Constrains the data types
    """
    area_field_required = "false"
admin.site.register(AreaTax, AreaTaxAdmin)
