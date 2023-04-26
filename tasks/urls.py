from django.urls import path
from .views import TaskListAPIView, TaskAPIRetriveAPIView, TaskCreateAPIView

urlpatterns = [
    path('list/', TaskListAPIView.as_view()),
    path('<int:pk>/', TaskAPIRetriveAPIView.as_view()),
    path('create/', TaskCreateAPIView.as_view()),
]
    
