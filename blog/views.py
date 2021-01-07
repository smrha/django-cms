from django.shortcuts import render, redirect

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
		form = NewPostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('post_list')
		else:
			return render(request, 'dashboard/post-new.html', {'form': form})
	else:
		form = NewPostForm()
		context = {
			'form': form
		}
	return render(request, 'dashboard/post-new.html', context)