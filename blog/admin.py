# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import blog
# Register your models here.
#admin.site.register(blog)
class BlogsAdmin(admin.ModelAdmin):
	list_display=('title','slug','author','publish','status')
	list_filter =('status','created','publish','author')
	search_fields = ('title','fields')
	prepopulated_fields={'slug':('title',)}
	raw_id_fields=('author',)
	date_hierarchy='publish'
	ordering=['status','publish']
admin.site.register(blog,BlogsAdmin)
