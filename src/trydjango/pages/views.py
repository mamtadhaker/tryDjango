from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
  print(request)
  print(args,kwargs)
  return  render(request,"home.html",{})

def contact_view(request,*args, **kwargs):
  # return HttpResponse("<h1>Contact page</h1>")
  return  render(request,"contact.html",{})

def about_us_view(request,*args, **kwargs):
  # return HttpResponse("<h1>About us page</h1>")
  return  render(request,"aboutus.html",{})

def social_view(request,*args, **kwargs):
  # return HttpResponse("<h1>Social view page</h1>")
  return  render(request,"social.html",{})
