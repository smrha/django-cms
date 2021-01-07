from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
	title = forms.CharField(
		label='عنوان پست :',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control'
				}
			)
		)
	content = forms.CharField(
		label='محتوای پست :',
		widget=forms.Textarea(
			attrs={
				'class': 'form-control'
				}
			)
		)
	slug = forms.SlugField(
		label='آدرس اینترنتی پست :',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control'
				}
			),
		error_messages={
			'invalid': 'یک آدرس اینترنتی معتبر شامل اعداد، حروف، - یا _ وارد کنید.',
			'valid': 'پست با این آدرس اینترنتی وجود دارد.'
			}
		)

	class Meta:
		model = Post 
		fields = ['title', 'content', 'slug']