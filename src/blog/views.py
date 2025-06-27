from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.http import Http404
from .forms import BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

# Create your views here.



def blog_post_list_view(request):
  # List out objects
  # Couldbe search
  qs= BlogPost.objects.all()
  template_name = 'blog/list.html'
  context = {"object_list": qs}
  return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
  # Create objects
  # Using a form
  form = BlogPostModelForm(request.POST or None)
  if form.is_valid():
    obj = form.save(commit=False)
    obj.user = request.user
    obj.save()
    form = BlogPostModelForm()
  template_name = 'form.html'
  context = {"form": form}
  return render(request, template_name, context)

def blog_post_detail_view(request, slug):
  # 1 object or detail view
  obj = get_object_or_404(BlogPost, slug=slug)
  template_name = 'blog/detail.html'
  context = {"object": obj}
  return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    
    if request.method == "POST":
        form = BlogPostModelForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('blog-detail', slug=obj.slug)  # Usa el nombre de la URL
        else:
            print("Errores del formulario:", form.errors)
    else:
        form = BlogPostModelForm(instance=obj)
    
    template_name = 'form.html'
    context = {
        "title": f"Update {obj.title}",
        "form": form,
    }
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
  obj = get_object_or_404(BlogPost, slug=slug)
  template_name = 'blog/delete.html'
  if request.method == "POST":
    obj.delete()
    return redirect('/blog/')
  context = {"object": obj}
  return render(request, template_name, context)
