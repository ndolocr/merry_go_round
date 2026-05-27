from django.urls import path

from user_management import views

app_name = "members"

urlpatterns = [
    path("view/all", views.view_all, name="view_all"),
]