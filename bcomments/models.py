# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# from django.contrib.auth.models import User


class Comments(MPTTModel):
    title = models.CharField("Title", max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    body = models.TextField("Body")
    username = models.CharField("User Name", max_length=50, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['date_create']

    def save(self, *args, **kwargs):
        if self.user:
            self.username = self.user.username
        super(Comments, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
