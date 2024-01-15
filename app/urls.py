from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('create/', create, name='create'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),

    path('get/', BaseViewClosed.as_view(), name='getClass'),
    path('createClass/', BaseViewCreate.as_view(), name='createClass'),
    path('detail/<int:pk>/', BaseViewDetail.as_view(), name='detailClass'),
    path('updateClass/<int:pk>/', BaseViewUpdate.as_view(), name='updateClass'),
    path('deleteClass/<int:pk>/', BaseViewDelete.as_view(), name='deleteClass'),

    path('list/', List.as_view(), name='getList'),
    path('detailView/<int:pk>/', Detail.as_view(), name='detailView'),
    path('createViewClass/', CreateViewClass.as_view(), name='createViewClass'),
    path('updateViewClass/<int:pk>/', UpdateViewClass.as_view(), name='updateViewClass'),
    path('deleteViewClass/<int:pk>/', DeleteViewClass.as_view(), name='deleteViewClass'),

]
