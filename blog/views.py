# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from .models import blog
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import EmailPostForm
from django.core.mail import send_mail

# Create your views here.
class PostListView(ListView):
	queryset =blog.published.all()
	context_object_name='posts'
	paginate_by=3
	template_name='blog/post/list.html'



def post_list(request):
	object_list = blog.published.all()
	paginator=Paginator(object_list,3)
	page = request.GET.get('page')
	try:
		posts=paginator.page(page)
	except PageNotAnInteger:
		posts=paginator.page(1)
	except EmptyPage:
		posts=paginator.page(paginator.num_pages)
	return render(request,'blog/post/list.html',{'page':page,'posts':posts})
def post_detail(request,year,month,day,post):
	post=get_object_or_404(blog,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
	return render(request,'blog/post/detail.html',{'post':post})
def post_share(request,post_id):
	# Retrieve post by id
	post = get_object_or_404(blog,id=post_id,status='published')
	sent=False

	if request.method == 'POST':
		# form was submitted
	    form = EmailPostForm(request.POST)
	    if form.is_valid():
			cd = form.cleaned_data
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject='{}({}) recommends you reading "{}"'
format(cd['name'],cd['email'],post.title)
	        message ='Read "{}" at {} \n \n {}\'s comments:{}'.
format(post.title,post_url,cd['name'],cd['comments'])
	        send_mail(subject,message,'admin@myblog.com',
[cd['to']])
					   sent = True

	 else:
	    	form = EmailPostForm()
	    return render(request,'blog/post/share.html',{'post':post,'form':form})
