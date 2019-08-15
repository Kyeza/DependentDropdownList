from django.urls import path

from . import views

app_name = 'erp'
urlpatterns = [
    path('', views.index, name='home')
]
