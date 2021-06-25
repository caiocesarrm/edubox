from django.urls import path

from edubox.base import views

urlpatterns = [

    path("posts/", view=views.PostsListCreate.as_view()),

    path("posts/<int:pk>/", view=views.PostDetail.as_view()),

    path("courses/", view=views.CourseListCreate.as_view()),

    path("courses/<int:pk>/", view=views.CourseDetail.as_view()),

    path("assignments/", view=views.AssignmentListCreate.as_view()),

    path("assignments/<int:pk>/", view=views.AssignmentDetail.as_view()),

]
