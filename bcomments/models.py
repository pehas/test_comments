# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.template.loader import render_to_string
from mptt.models import MPTTModel, TreeForeignKey
# from django.contrib.auth.models import User


class Comments(MPTTModel):
    username = models.CharField("User Name", max_length=50, blank=True)
    title = models.CharField("Title", max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    body = models.TextField("Body")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['-date_create']

    class Meta:
        ordering = ['-date_create']

    def save(self, *args, **kwargs):
        if self.user:
            self.username = self.user.username
        super(Comments, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def recursive_node_to_dict(self):
        result = {
            'id': self.pk,
            'username': self.username,
            'title': self.title,
            'body': self.body,
        }
        children = [self.recursive_node_to_dict(c) for c in self.get_children()]
        if children:
            result['children'] = children
        return result

    def html_block(self):
        return render_to_string('blocks/tree_comments.html', context={
            'comment': self.get_descendants(include_self=True)
        })