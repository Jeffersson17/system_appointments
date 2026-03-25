from rest_framework import serializers

from enterprise.models import Enterprise
from user.models import User
from user.serializers import UserSerializer


class EnterpriseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Enterprise
        fields = ["id", "company_name", "owner_name", "logotipo", "user", "password", "email"]

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
        else:
            fields.pop("email", None)
            fields.pop("password", None)
        return fields
