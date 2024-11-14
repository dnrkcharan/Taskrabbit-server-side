from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    # path("something", views.index, name="index"),
    path("login/", LoginAPI.as_view(), name ="login"),
    path("signup/", SignupAPI.as_view(), name ="login"),

]