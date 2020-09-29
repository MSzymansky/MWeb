from django.urls import path
from django.contrib.auth import views as auth_views
from groups import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('posts/in/(?P<slug>[-\w]+)/', views.SingleGroup.as_view(), name='single'),
]
