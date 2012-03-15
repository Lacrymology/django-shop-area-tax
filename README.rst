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
Add 'area_tax' to INSTALLED_APPS and 'area_tax.modifiers.AreaTaxModifier' to
your SHOP_CART_MODIFIERS list.
