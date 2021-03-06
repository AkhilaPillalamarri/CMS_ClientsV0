from django.urls import path
from . import views
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)


urlpatterns = [

    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('', ClientListView.as_view(), name='client_list'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('<int:pk>/newcomment/', CommentCreateView.as_view(), name='comment_new'),
    path('<int:pk>/commentedit/',
         CommentUpdateView.as_view(), name='comment_edit'),
    path('<int:pk>/commentdelete/',
         CommentDeleteView.as_view(), name='comment_delete'),


]
