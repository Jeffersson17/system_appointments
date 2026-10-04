from rest_framework import serializers

from clients.models import Client
from user.models import User
from user.serializers import UserSerializer
from enterprise.serializers import EnterpriseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied


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

    def update(self, instance, validated_data):
        request = self.context.get("request")
        if request.user.role not in ["ENTERPRISE", "ADMIN"]:
            return PermissionDenied("Você não tem permissão para atualizar clientes.")
        if request.user.role == "ENTERPRISE" and request.user.enterprise != instance.enterprise:
            return PermissionDenied("Você não tem permissão para atualizar clientes de outra empresa.")
        password = validated_data.pop("password", None)
        if password:
            instance.user.set_password(password)
            instance.user.save()
        return super().update(instance, validated_data)

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method in ["POST"]:
            fields["email"].required = True
            fields["password"].required = True
        return fields

    def validate_phone_number(self, value):
        queryset = Client.objects.filter(phone_number=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError("Este número de telefone já está registrado. Tente outro numero.")
        return value
