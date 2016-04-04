from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents')

@python_2_unicode_compatible
class Msg(models.Model):
    user = models.CharField(max_length=100)
    public = models.CharField(max_length=100)
    encmsg = models.TextField()
    decmsg = models.TextField()
	
    def __str__(self):
            return '%s %s ' % (self.public, self.encmsg)