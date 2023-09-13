# TodoApi
first i install django and django rest framework
create new app in the project
then add the app and django restframwork in seetings for the project
add the app in the urls.py of the project
Add model in the app which contain the fields of the Todo list (title,Iscomplete)
add file serializers.py in app folder to link it with the model which added 
in the views add classes based views using these resources 

https://www.django-rest-framework.org/tutorial/3-class-based-views/
https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-the-url

By entering this path 'POST/todos/' You can create new tasks in TodoApp
By entering this path 'GET/todos/' You can show all the tasks in TodoApp
By entering this path 'GET/todos/<int:pk>/' or 'PUT/todos/<int:pk>/' you can show specific Task or update the task 
By entering this path 'Delete/todos/<int:pk>/' you can delete specific task
By entering this path 'Get/todos/search/' then write the the task you want search for it in url to show task
By entering this path 'Get/todos/filter/' show the tasks which completed already

