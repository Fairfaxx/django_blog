from  django import forms

class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
