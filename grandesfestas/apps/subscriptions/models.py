# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from volunteers.models import Volunteer
from trainings.models import Training


class Subscription(models.Model):
    PAYMENT = (
        ('Cash', _("cash")),
        ('Eletronic', _("eletronic")),
    )
    created_date = models.DateTimeField(_('Created date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified date'), auto_now=True, editable=False)

    volunteer = models.ForeignKey(Volunteer, verbose_name=_('Volunteer'))
    training = models.ForeignKey(Training, verbose_name=_('Training'), null=True, blank=True)
    present = models.BooleanField(_('Present in training'), default=False)
    paid = models.FloatField(_('Paid'), default=0)
    payment = models.CharField(_('Payment'), choices=PAYMENT, max_length=16, blank=True)
    extra = models.PositiveSmallIntegerField(_('Extra value'), default=0)
    valid = models.BooleanField(_('Valid'), default=False)

    class Meta:
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')
