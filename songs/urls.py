from django.urls import path
from . import views

urlpatterns = [
    path('', views.SongList.as_view()),
    path('<int:pk>/', views.SongDetail.as_view())
]