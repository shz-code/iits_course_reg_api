from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("quizzes", views.getQuizzes),
    path("deadline", views.getDeadline),
    path("submitQuiz", views.submitQuiz)
]
