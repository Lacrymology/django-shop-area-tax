DESCRIPTION
===========

This is an area tax Cart Modifier for django-shop (www.django-shop.org). It
provides a way of taxing the clients according to their address, either billing
or shipping.

It will work on the cart total, so if you need to tax shipping costs, place
the modifier after the shipping modifiers on the list.

Requirements
------------
uses django-shop-l10n ( https://github.com/Lacrymology/django-shop-l10n ) for
Area definitions

Usage
-----
Add "area_tax" to INSTALLED_APPS and "area_tax.modifiers.AreaTaxModifier" to
your SHOP_CART_MODIFIERS list.

You'll also need to run `./manage.py syncdb` (or `./manage.py migrate area_tax`
if you use south).

area_tax will look for ONE Country (`l10n.models.Country`), and ONE AdminArea
to calculate taxes. If the `area_tax.models.AreaTax` instance is marked as
compound (and it refers to an AdminArea), the tax will be calculated on top of
the total current price. Otherwise, the subtotal will be used.

Likewise, if the `area_tax.models.AreaTax` is marked to override National Tax,
the Country Tax calculation will be skipped.

Admin
-----
The Area fieldin the AreaTax model is optional. If left blank, you're setting
the country-wide tax. Otherwise, you're setting the area's tax, and it will
behave as describe above about compounding and overrides.

Settings
--------
All settings go inside a dictionary named DJANGO_SHOP_AREA_TAX in your
settings.py file.
TAX_SHIPPING_ADDRESS (default True). True, if you want the tax
calculated from shipping address. False will calculate it based on billing
addresss instead.

e.g:
DJANGO_SHOP_AREA_TAX = { 'TAX_SHIPPING_ADDRESS': False, }

WARNING
-------
If you use the provided fixtures, beware that the objects' IDs might conflict
in them.
