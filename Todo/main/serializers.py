from rest_framework import serializers
from .models import Task

class Todo(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('id','title','iscomplete')