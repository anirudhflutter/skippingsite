from django.urls import path

from .views import add,products,optionsPage


urlpatterns = [
    path("signup/", add, name="register"),
    path("products/",products,name = "productdata"),
    path("options/",optionsPage,name = "optionsdata")
]