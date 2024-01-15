from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('create/', CreateViewClass.as_view(), name='create'),

]
