from django.urls import path

from . import views


urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('orders/', views.OrdersListView.as_view()),
    path('create_product/', views.ProductCreateView.as_view()),
    path('hand_made_orders/', views.HandMadeOrdersListView.as_view()),
    path('users/', views.UsersListView.as_view()),
    path('images/', views.ImageListView.as_view())
]
