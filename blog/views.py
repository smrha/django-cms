from django.shortcuts import render, redirect
from datetime import datetime
import pytz

from .models import Post

from .forms import NewPostForm

def index(request):
	return render(request, 'dashboard/index.html')

def post_list(request):
	posts = Post.objects.all()
	context = {
		'posts': posts
	}
	return render(request, 'dashboard/post-list.html', context)

def post_new(request):
	if request.method == 'POST':
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('post_list')
		else:
			return render(request, 'dashboard/post-form.html', {'form': form})
	else:
		form = NewPostForm()
		context = {
			'form': form
		}
	return render(request, 'dashboard/post-form.html', context)

def post_edit(request, pk):
	if request.method == "POST":
		post = Post.objects.get(id=pk)
		form = NewPostForm(request.POST or None, request.FILES or None, instance=post)
		if form.is_valid():
			form.save()
			return redirect('post_list')
		else:
			return render(request, 'dashboard/post-form.html', {'form': form})
	else:
		post = Post.objects.get(id=pk)
		form = NewPostForm(instance=post)
		context = {
			'form': form
		}
		return render(request, 'dashboard/post-form.html', context)