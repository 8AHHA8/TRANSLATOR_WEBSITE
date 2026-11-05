from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.page_detail, name='page'),
]