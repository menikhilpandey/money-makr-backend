""" Views for Main """

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Wallet, Category, Event, Budget, Transaction
from .serializers import WalletSerializer, CategorySerializer, EventSerializer, BudgetSerializer, TransactionSerializer


class WalletListCreateView(ListCreateAPIView):
    """ Wallet ListCreateAPIView """
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """ Wallet RetrieveUpdateDestroyAPIView """
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = "name"
