# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from bcomments.models import Comments
from bcomments.views import CommentsForm

register = template.Library()


@register.inclusion_tag('blocks/modal_block.html', takes_context=True)
def modal_comment_form(context):

    form = CommentsForm(initial={
        'user': context.request.user if context.request.user.is_authenticated() else None
    })
    return locals()
