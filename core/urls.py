from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('write_post', write_post, name='write_post')
]
