from django.urls import path

from users import views

app_name = "members"

urlpatterns = [
    path("view/all", views.view_all, name="view_all"),
]