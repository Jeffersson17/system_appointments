from rest_framework import serializers

from clients.models import Client
from user.models import User
from user.serializers import UserSerializer


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = ["id", "first_name", "last_name", "phone_number", "enterprise", "user", "email", "password"]

    def create(self, validated_data):
        email = validated_data.pop("email")
        password = validated_data.pop("password")
        user = User.objects.create_user(
            name=f"{validated_data['first_name']} {validated_data['last_name']}", email=email, password=password
        )
        client = Client.objects.create(user=user, **validated_data)
        return client
