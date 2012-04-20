from decimal import Decimal

from shop.cart.cart_modifiers_base import BaseCartModifier
from shop.models import AddressModel

from area_tax import settings
from area_tax import models

class MultipleFieldCartModifier(BaseCartModifier):
    """
    A cart modifier that allows get_extra_cart_field and
    get_extra_cart_item_field to return list of tuples instead of a single one
    """
    def process_cart(self, cart, state):
        """
        Allows processing list of (label, value) tuples instead of a single one
        """
        fields = self.get_extra_cart_price_field(cart)
        if fields:
            if isinstance(fields[0], basestring):
                # single tuple
                fields = [fields]

            for field in fields:
                price = field[1]
                cart.current_total += price
                cart.extra_price_fields.append(field)
        return cart
                    
    def process_cart_item(self, cart_item, state):
        """
        Allows processing list of (label, value) tuples instead of a single one
        """
        fields = self.get_extra_cart_item_price_field(cart_item)
        if fields:
            if isinstance(fields[0], basestring):
                # single tuple
                fields = [fields]
            for field in fields:
                price = field[1]
                cart_item.current_total = cart_item.current_total + price
                cart_item.extra_price_fields.append(field)
        return cart_item

class AreaTax(MultipleFieldCartModifier):
    """
    Applies a tax according to the buyer's location
    """
    def get_extra_cart_price_field(self, cart):
        """
        """
        zero = Decimal("0.00")

        if not cart.user:
            return None
        
        try:
            address = (cart.user.shipping_address
                       if settings.DJANGO_SHOP_AREA_TAX['TAX_SHIPPING_ADDRESS']
                       else cart.user.billing_address)
        except AddressModel.DoesNotExist:
            return None

        try:
            area_tax = models.AreaTax.objects.get(country=address.country,
                                                  area=address.state,)
        except models.AreaTax.DoesNotExist:
            area_tax = None

        if area_tax and area_tax.override_national:
            return (area_tax.name, cart.current_total * area_tax.percentage)

        tax_values = []
        tax_names = []

        try:
            country_tax = models.AreaTax.objects.get(country=address.country,
                                                     area=None)
        except models.AreaTax.DoesNotExist:
            country_tax = None

        if country_tax:
            tax_names.append("%s (%s%%)" % (
                    country_tax.name,
                    (country_tax.percentage * 100).quantize(zero)))
            tax_values.append(country_tax.percentage * cart.current_total)

        if area_tax:
            tax_names.append("%s (%s%%)" % (
                    area_tax.name,
                    (area_tax.percentage * 100).quantize(zero)))
            if area_tax.is_compound:
                tax_values.append(area_tax.percentage * (cart.current_total +
                                                         tax_values[0]))
            else:
                tax_values.append(area_tax.percentage * cart.current_total)
        tax_values = [value.quantize(zero) for value in tax_values]
        return zip(tax_names, tax_values)
