from django.contrib import admin
from area_tax.models import AreaTax

from l10n.admin import CountryAreaAdmin

class AreaTaxAdmin(CountryAreaAdmin):
    """
    Admin class for AreaTax. Constrains the data types
    """
    area_field_required = "false"
    list_display = ("name", "country", "area", "percentage", "is_compound",
                    "override_national")
    list_editable = ("percentage", "is_compound", "override_national")
    ordering = ("country", "area")

admin.site.register(AreaTax, AreaTaxAdmin)
