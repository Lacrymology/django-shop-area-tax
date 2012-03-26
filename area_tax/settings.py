from django.conf import settings

DJANGO_SHOP_AREA_TAX = {
    'TAX_SHIPPING_ADDRESS': True,
    }

DJANGO_SHOP_AREA_TAX.update(getattr(settings, 'DJANGO_SHOP_AREA_TAX', {}))
settings.DJANGO_SHOP_AREA_TAX = DJANGO_SHOP_AREA_TAX
