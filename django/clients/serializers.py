from rest_framework import serializers

from clients.models import Client
from user.models import User
from user.serializers import UserSerializer
from enterprise.serializers import EnterpriseSerializer
from rest_framework.response import Response
from rest_framework import status


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    email = serializers.EmailField(write_only=True)
    enterprise = EnterpriseSerializer(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = ["id", "first_name", "last_name", "phone_number", "enterprise", "user", "email", "password"]

    def create(self, validated_data):
        request = self.context.get("request")
        email = validated_data.pop("email")
        password = validated_data.pop("password")
        enterprise = request.user.enterprise
        user = User.objects.create_user(
            name=f"{validated_data['first_name']} {validated_data['last_name']}", email=email, password=password
        )
        client = Client.objects.create(user=user, enterprise=enterprise, **validated_data)
        return client

    def destroy(self, request, *args, **kwargs):
        if request.user.role not in ["ENTERPRISE", "ADMIN"]:
            return Response(
                {"detail": "Você não tem permissão para excluir clientes."},
                status=status.HTTP_403_FORBIDDEN,
            )
        if request.user.role == "ENTERPRISE" and request.user.enterprise != self.get_object().enterprise:
            return Response(
                {"detail": "Você não tem permissão para excluir clientes de outra empresa."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method in ["POST"]:
            fields["email"].required = True
            fields["password"].required = True
        else:
            fields.pop("email", None)
            fields.pop("password", None)
        return fields

    def validate_phone_number(self, value):
        if Client.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Ja existe um cliente com esse número de telefone. Digite outro número.")
        return value
