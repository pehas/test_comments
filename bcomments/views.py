# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm, HiddenInput
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Comments


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        widgets = {
            'user': HiddenInput(),
            'parent': HiddenInput(),
        }


def index_page(request):
    comments = Comments.objects.filter(parent__isnull=True)
    return render(request, 'index_page.html', locals())


def comment_page(request, comment_id=None):
    comment = get_object_or_404(Comments, id=comment_id)
    return render(request, "comment_page.html", locals())


def comment_add_page(request, comment_id=None):
    comment = None
    if comment_id:
        comment = get_object_or_404(Comments, id=comment_id)

    form = CommentsForm(request.POST or None, initial={
        'parent': comment,
        'user': request.user if request.user.is_authenticated() else None
    })
    if request.method == "POST":
        if form.is_valid():
            c = form.save(commit=False)
            c.parent = comment
            c.user = request.user if request.user.is_authenticated() else None
            c.save()
            if request.is_ajax():
                return JsonResponse({
                    'message': "ok",
                    "result": c.recursive_node_to_dict(),
                    "result_html": c.parent.html_block()
                }, status=200)
            else:
                return redirect(reverse('index_page'))
        else:
            if request.is_ajax():
                return JsonResponse({'message': "Error"}, status=500)

    return render(request, 'add_comment_page.html', locals())





