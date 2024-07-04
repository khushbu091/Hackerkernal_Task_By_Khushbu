from rest_framework import serializers
from .models import User, Task

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"


class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"