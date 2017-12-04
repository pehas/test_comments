# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Comments


class CommentsAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'username', 'date_create', 'date_update')
    list_display_links = ('indented_title', )
    search_fields = ('tile', )
    list_filter = ('date_create', 'date_update')
    date_hierarchy = 'date_create'


admin.site.register(Comments, CommentsAdmin)
