from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('user_login/', views.user_login, name="user_login"),
    path('register/', views.register, name="register"),

    path('user_logout/', views.user_logout, name="user_logout"),
    path('special/', views.special, name="special")
]
