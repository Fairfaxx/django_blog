from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
  title = "Hello, world. You're at the home page"
  context = {"title": title}
  return render(request, "home.html", context)

def about_page(request):
  return render(request, "about.html", {"title": "About Us!"})

def contact_page(request):
  form = ContactForm(request.POST or None)
  if form.is_valid():
    print(form.cleaned_data)
    form = ContactForm()
  context = {"title": "Contact Us", "form": form}
  return render(request, "form.html", context)
