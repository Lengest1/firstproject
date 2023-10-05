from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path ('posts/',views.posts_list),
    path ('posts/<int:index>',views.posts_details),
    path ('groups',views.groups_list),
    path ('groups/<slug:any>',views.group_info),
]





# path ('posts/',views.posts_list),
# path ('posts/<index>',views.posts_details),