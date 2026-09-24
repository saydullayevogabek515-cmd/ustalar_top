from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "customer",
            "master",
            "services",
            "title",
            "description",
            "address",
            "city",
            "schedule_at",
            "price",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "customer",
            "price",
            "status",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        request = self.context["request"]

        if request.user.role != "CUSTOMER":
            raise serializers.ValidationError(
                "Faqat xaridorlar buyurtma yaratishi mumkin"
            )

        master = attrs.get("master")
        service = attrs.get("service")

        if not master:
            raise serializers.ValidationError({"master": "Usta tanlanishi shart"})

        if not service:
            raise serializers.ValidationError({"service": "Xizmat tanlanishi shart"})

        if not master.is_available:
            raise serializers.ValidationError("Usta hozir mavjud emas")

        if service.master != master:
            raise serializers.ValidationError(
                "Tanlangan xizmat ushbu ustaga tegishli emas"
            )

        return attrs

    def create(self, validated_data):
        request = self.context["request"]

        validated_data["customer"] = request.user

        validated_data["price"] = validated_data["service"].price

        return super().create(validated_data)