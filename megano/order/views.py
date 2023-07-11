from rest_framework import generics
from .models import Order, BasketItem
from .serializers import OrderSerializer, BasketItemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'


class UpdateOrderView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'



class BasketItemView(generics.ListAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer


class AddToBasketView(generics.CreateAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer


class ClearBasketView(generics.DestroyAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer



class PaymentView(APIView):
    def post(self, request):
        number = request.data.get('number')
        name = request.data.get('name')
        month = request.data.get('month')
        year = request.data.get('year')
        code = request.data.get('code')

        # Здесь выполняется логика обработки платежей
        # Вы можете интегрироваться с платежным шлюзом или выполнять любые необходимые проверки

        # Предполагая, что платеж прошел успешно, вы можете вернуть ответ об успехе
        return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)

        # Если платеж не прошел или возникла какая-либо ошибка, можно вернуть ответ об ошибке.
        # return Response({'message': 'Payment failed'}, status=status.HTTP_400_BAD_REQUEST)
