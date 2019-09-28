from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'bksbk'

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('login/',
         auth_views.LoginView.as_view(template_name='registration/login.html'),
         name='login'),
    # path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', include('django.contrib.auth.urls')),
]
