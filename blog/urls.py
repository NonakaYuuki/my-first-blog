from django.urls import path
from . import views
urlpatterns = [
    path('', views.tokyo_list, name='tokyo_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('tokyo/bunkyo/',views.bunkyo_list,name='bunkyo_list'),
    path('tokyo/bunkyo/juntendo/',views.bunkyo_juntendo,name='bunkyo_juntendo'),
]