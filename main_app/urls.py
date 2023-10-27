from django.urls import include, path
from . import views


app_name = "main_app"

urlpatterns = [
    path("", views.home, name="home"),
    # path("login_user", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logout_user"),
    path("register", views.register_user, name="register_user"),
    path("record/<int:id>", views.add_record, name="record"),
]
