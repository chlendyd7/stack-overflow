from rest_framework import serializers
from service.models import User

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        write_only = False

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
