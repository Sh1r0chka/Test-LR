from django.contrib.auth.models import User
from .models import Orders, Services
from .serializers import OrderSerializer, UserSerializer, ServecesSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly


# Информация о пользователях
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Заявки
class OrdersList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


# Сервисы
class Services(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
