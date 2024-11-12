from django.urls import path
from .views import TodoAPIView

urlpatterns = [
    path('todos/', TodoAPIView.as_view()),              # List all,Create - GET - POST
    path('todos/<int:id>/', TodoAPIView.as_view()),     # Retrieve, Update, Delete - GET - PUT - DELETE
]
