# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from .models import blog


# Create your views here.
def post_list(request):
	posts=blog.published.all()
	return render(request,'blog/post/list.html',{'posts':posts})
def post_detail(request,year,month,day,post):
	post=get_object_or_404(blog,slug=post,status='published',publish_year=year,publish_month=month,publish_day=day)
	return render(request,'blog/post/details.html',{'post':post})