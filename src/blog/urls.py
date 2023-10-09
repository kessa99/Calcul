from django.urls import path
from . import views


urlpatterns = [
    path('index_blog/', views.index_blog, name='index_blog'),
]