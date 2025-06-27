from  django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title=title)
        if self.instance is not None:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title has already been used.")
        return title
