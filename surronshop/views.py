from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import Product, Order, HandMadeOrder, Customer, Image
from .serializers import (
    ProductListSerializer,
    OrdersListSerializer,
    ProductCreateSerializer,
    HandMadeOrderListSerializer,
    UserListSerializer,
    ImageListSerializer
)


class ProductListView(APIView):
    """Вывод списка товаров"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        products = Product.objects.filter(draft=False)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductCreateView(APIView):
    """Добавление товара"""
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        product = ProductCreateSerializer(data=request.data)
        product.is_valid(raise_exception=True)
        product.save()
        return Response(status=201)


class OrdersListView(APIView):
    """Вывод списка заказов"""

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrdersListSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        order = OrdersListSerializer(data=request.data)
        order.is_valid()
        order.save()
        return Response(status=201)


class HandMadeOrdersListView(APIView):
    """Вывод заказов, сделанных вручную"""

    def get(self, request):
        h_m_orders = HandMadeOrder.objects.all()
        serializer = HandMadeOrderListSerializer(h_m_orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        h_m_order = HandMadeOrderListSerializer(data=request.data)
        h_m_order.is_valid()
        h_m_order.save()
        return Response(status=201)


class UsersListView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        users = Customer.objects.filter()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class ImageListView(APIView):

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageListSerializer(images, many=True)
        return Response(serializer.data)
