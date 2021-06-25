from django.urls import path

from edubox.users import views

app_name = "users"
urlpatterns = [

    path("", view=views.CreateAuthUserView.as_view()),
]
