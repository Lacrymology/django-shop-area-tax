from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from l10n.models import Country, AdminArea

class LocalTax(models.Model):
    """
    One area's tax
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    area = generic.GenericForeignKey()
