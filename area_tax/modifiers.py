from shop.cart.cart_modifiers_base import BaseCartModifier
from decimal import Decimal

from area_tax import settings
from area_tax import models

class AreaTax(BaseCartModifier):
    """
    Applies a tax according to the buyer's location
    """
    def get_extra_cart_price_field(self, cart):
        """
        """
        address = (cart.user.shipping_address
                   if settings.DJANGO_SHOP_AREA_TAX['TAX_SHIPPING_ADDRESS']
                   else cart.user.billing_address)
        try:
            area_tax = models.AreaTax.objects.get(country=address.country,
                                                  area=address.state,)
        except models.AreaTax.DoesNotExist:
            area_tax = None

        tax_value = 0
        tax_names = []
        if area_tax and area_tax.override_national:
            return (area_tax.name, cart.current_total * area_tax.percentage)

        try:
            country_tax = models.AreaTax.objects.get(country=address.country,
                                                     area=None)
        except models.AreaTax.DoesNotExist:
            country_tax = None

        if country_tax:
            tax_names.append(country_tax.name)
            tax_value = country_tax.percentage * cart.current_total

        if area_tax:
            tax_names.append(area_tax.name)
            if area_tax.is_compound:
                tax_value += area_tax.percentage * (cart.current_total +
                                                   tax_value)
            else:
                tax_value += area_tax.percentage * cart.current_total
        return ("+".join(tax_names), tax_value.quantize(Decimal("0.00")))
