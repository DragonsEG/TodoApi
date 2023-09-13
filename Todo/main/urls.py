from django.urls import path
from . import views
from .views import TodoList,TaskDetails,CreateTask,DeleteTask,filter,search

urlpatterns=[
    ##path('',views.index,name='index')
    path('GET/todos/',TodoList.as_view()),
    path('GET/todos/<int:pk>/',TaskDetails.as_view()),
    path('PUT/todos/<int:pk>/',TaskDetails.as_view()),
    path('POST/todos/',CreateTask.as_view()),
    path('Delete/todos/<int:pk>/',DeleteTask.as_view()),
    path('Get/todos/filter/',filter.as_view()),
    path('Get/todos/search/',search.as_view()),

]