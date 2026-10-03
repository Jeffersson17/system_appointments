from rest_framework import serializers

from enterprise.models import Enterprise
from user.models import User
from user.serializers import UserSerializer


class EnterpriseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    email = serializers.EmailField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    is_active = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = Enterprise
        fields = ["id", "company_name", "owner_name", "logotipo", "user", "password", "email", "is_active"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        email = validated_data.pop("email")
        user = User.objects.create_user(
            name=validated_data["owner_name"], email=email, password=password, role="ENTERPRISE"
        )
        enterprise = Enterprise.objects.create(user=user, **validated_data)
        return enterprise

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method in ["POST"]:
            fields["email"].required = True
            fields["password"].required = True
        return fields
    
    def update(self, instance, validated_data):
        email = validated_data.pop("email", None)
        is_active = validated_data.pop("is_active", None)
        password = validated_data.pop("password", None)
        instance = super().update(instance, validated_data)

        if email is not None:
            instance.user.email = email

        if is_active is not None:
            instance.user.is_active = is_active

        if password is not None:
            instance.user.set_password(password)

        instance.user.save()

        return instance
