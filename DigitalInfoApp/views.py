from django.shortcuts import redirect, render
from .models import *

default_dict = { "acc_pages": ["index","index_2","forgot_pwd","profile_page"]}

def index(request):
    default_dict["current_page"] = "index"
    return render(request,"index.html",default_dict)

def index_2(request):
    default_dict["current_page"] = "index_2"
    return render(request, "index_2.html",default_dict)

def login_page(request):
    default_dict["current_page"] = "login_page"
    return render(request, "login_page.html", default_dict)

def register_page(request):
    default_dict["current_page"] = "register_page"
    return render(request,"register_page.html",default_dict)

def forgot_pwd(request):
    default_dict["current_page"] = "forgot_pwd"
    return render(request,"forgot_pwd.html",default_dict)

def profile_page(request):
    default_dict["current_page"] = "profile_page"
    return render(request,"profile_page.html",default_dict)
   
