from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("callback/", views.callback_handling, name="callback"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout, name="logout"),
    path("", views.home, name="home"),
]
