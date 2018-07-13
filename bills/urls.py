from django.urls import path
from . import views


urlpatterns = [
    path('', views.bill_page, name='Bills')
]