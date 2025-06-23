from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
  title = "Hello, world. You're at the home page"
  context = {"title": title}
  return render(request, "home.html", context)

def about_page(request):
  return render(request, "about.html", {"title": "About Us!"})

def contact_page(request):
  return render(request, "hello_world.html", {"title": "Contact Us"})
