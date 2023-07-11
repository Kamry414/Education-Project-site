from django.urls import path
from orders import views


urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/<int:id>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('basket/', views.BasketItemView.as_view(), name='basket'),
    path('payment/<int:id>/', views.PaymentView.as_view(), name='payment'),
]
