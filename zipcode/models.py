# -*- coding: utf-8 -*-
from django.db import models


class ZipCode(models.Model):
    zip_code = models.CharField(max_length=8)
    address = models.CharField(max_length=150, null=True, blank=True)
    neighborhood = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    
    class Meta:
        verbose_name = u'Zipcode'
        verbose_name_plural = u'Zipcodes'
        
    def __unicode__(self):
        return "%s" % self.zip_code
        