from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:user_id>/', views.profile, name='profile'),
]
