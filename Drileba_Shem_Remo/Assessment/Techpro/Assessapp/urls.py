from django.urls import path
from Assessapp import views
urlpatterns = [
  path('', views.index, name='index'),
]