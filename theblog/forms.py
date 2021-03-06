from django import forms
from .models import Post, Category
choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Here...'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Write Your Blog Here...'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Here...'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Write Your Blog Here...'}),
        }