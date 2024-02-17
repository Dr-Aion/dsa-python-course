from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aiganym", views.aiganym, name="aiganym"),
    path("<str:name>", views.greet, name="greet")

]