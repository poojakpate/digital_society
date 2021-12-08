from django.urls import path
from .views import *

urlpatterns=[
	path("",index),
	path("login_page/",login_page, name="login_page"),
	path("register_page/",register_page,name = "register_page"),
	path("forgot_pwd/",forgot_pwd,name = "forgot_pwd"),
	path("profile_page/",profile_page,name = "profile_page"),
	path("index_2/",index_2,name = "index_2"),
	]
	