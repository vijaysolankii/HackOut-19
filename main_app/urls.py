from django.urls import path
from .import views
urlpatterns = [
    path('',views.HomeView,name="home"),
    path('index2/',views.Index2,name="index2"),
    path('index3/',views.Index3,name="index3"),
    path('index4/',views.Index4,name="index4"),
    path('index5/',views.Index5,name="index5"),
    path('index6/',views.Index6,name="index6"),
    path('index7/',views.Index7,name="index7"),
    path('list/',views.list,name='list'),
    path('chat/', views.HomeView, name='chat')
]