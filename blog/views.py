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
		# update_data = request.POST.copy()
		# update_data.update({'publish': datetime.strptime(request.POST['publish'], '%Y/%m/%d %H:%M:%S')})
		mydata = request.POST.copy()
		mydata.update({'publish': pytz.utc.localize(datetime.strptime(request.POST['publish'], '%Y/%m/%d %H:%M:%S'))})
		print(mydata['publish'])
		form = NewPostForm(data=mydata) 
		print(form)
		
		# now_aware = pytz.utc.localize(unaware)
		# mydata['publish'] = datetime.strptime(request.POST['publish'], '%Y/%m/%d %H:%M:%S')
		
		print(form.is_valid())
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