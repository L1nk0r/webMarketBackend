from rest_framework import serializers

from .models import Product, Order, HandMadeOrder, Customer, User, Image


class ProductCreateSerializer(serializers.ModelSerializer):
    """Добавление продукта"""

    class Meta:
        model = Product
        fields = (
            "article",
            "title",
            "short_info",
            "info",
            "price",
            "slug",
            "in_stock",
            "availability",
        )


class ProductListSerializer(serializers.ModelSerializer):
    """Список товаров"""

    img = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = (
            "article",
            "title",
            "short_info",
            "info",
            "price",
            "img",
            "slug",
            "in_stock",
            "availability",
        )


class OrdersListSerializer(serializers.ModelSerializer):
    """Список заказов"""

    products = serializers.SlugRelatedField(slug_field="title", read_only=True, many=True)

    class Meta:
        model = Order
        fields = (
            "products",
            "date",
            "total_price",
            "address",
            "status",

            "name",
            "email",
            "phoneNumber",
            "city",
            "country",
            "zipCode",
        )

    def update(self, instance, validated_data):
        status = validated_data.get('status', instance.status)
        instance.status = status
        instance.save()
        return instance


class HandMadeOrderListSerializer(serializers.ModelSerializer):
    """Список заказов, сделанных в ручную"""

    class Meta:
        model = HandMadeOrder
        fields = (
            "name",
            "address",
            "email",
            "phoneNumber",
            "products",
            "total_price",
            "date",
            "status"
        )


class UserListSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field="username", read_only=True, many=False)
    orders = serializers.SlugRelatedField(slug_field="date", read_only=True, many=True)

    class Meta:
        model = Customer

        fields = (
            "role",
            "user",
            "phone",
            "address",
            "orders"
        )


class ImageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = (
            "__all__"
        )
