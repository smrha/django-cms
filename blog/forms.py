from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
	STATUS_CHOICES = (
		('d', 'پیش نویس'),
		('p', 'انتشار یافته'),
		)
	title = forms.CharField(
		label ='عنوان پست :',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control'
				}
			)
		)
	content = forms.CharField(
		label ='محتوای پست :',
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control'
				}
			)
		)
	slug = forms.SlugField(
		label ='آدرس اینترنتی پست :',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control'
				}
			),
		error_messages = {
			'invalid': 'یک آدرس اینترنتی معتبر شامل اعداد، حروف، - یا _ وارد کنید.',
			'valid': 'پست با این آدرس اینترنتی وجود دارد.'
			}
		)
	publish = forms.DateTimeField(
		label = 'تاریخ انتشار',
		widget = forms.DateTimeInput(
			attrs = {
				'class': 'form-control normal-example',
				'id': 'inputDate1'
				}
			)
		)
	status = forms.CharField(
		label = 'وضعیت انتشار :',
		widget = forms.Select(
			choices = STATUS_CHOICES,
			attrs = {
				'class': 'form-control'
				}
			)
		)
	thumbnail = forms.ImageField(
		label = '',
		widget = forms.FileInput(
			attrs = {
				'class': 'form-control'
				}
			)
		)

	class Meta:
		model = Post 
		fields = ['title', 'content', 'slug', 'publish', 'status']