from django.urls import path 

from . import views   # import views.py file form API Application  
urlpatterns = [
    path('', views.TaskList.as_view()),
	path('task-details/<int:pk>/', views.TaskDetail.as_view() ),
 
]
