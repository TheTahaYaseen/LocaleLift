from . import views
from django.urls import path

urlpatterns = [
    
    # Home Url
    path("", views.home_view, name="home"),
    
    # Auth Urls
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),

    # Business Profile Urls
    path("create_business_profile", views.create_business_profile_view, name="create_business_profile"),
    path("update_business_profile/<str:primary_key>", views.update_business_profile_view, name="update_business_profile"),
    path("delete_business_profile/<str:primary_key>", views.delete_business_profile_view, name="delete_business_profile"),

]