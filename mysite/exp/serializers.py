from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import lang

class LangSerializer(serializers.ModelSerializer):
    
    class Meta:
        Model = lang
        fields = "__all__"
        