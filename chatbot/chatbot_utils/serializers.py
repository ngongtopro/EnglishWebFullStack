from rest_framework import serializers
from chatbot.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'role', 'content', 'created_at']