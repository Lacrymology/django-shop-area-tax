from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from l10n.models import Country, AdminArea

class AreaTax(models.Model):
    """
    One area's tax
    """
    country = models.ForeignKey(Country, verbose_name=_("country"))
    area = models.ForeignKey(AdminArea, verbose_name=_("area"), null=True)

    class Meta:
        verbose_name = _("area tax")
        verbose_name_plural = _("area taxes")
