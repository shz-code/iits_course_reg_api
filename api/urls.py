from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("", views.index),
    path("quizzes", views.getQuizzes),
    path("deadline", views.getDeadline),
    path("submitQuiz", views.submitQuiz),
    path("submitForm", views.submitForm),
    path("download_student_list", views.download)
]
