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
    lookup_field = "slug"


class CategoryListCreateView(ListCreateAPIView):
    """ Category ListCreateAPIView """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """ Category RetrieveUpdateDestroyAPIView """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"


class EventListCreateView(ListCreateAPIView):
    """ Event ListCreateAPIView """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """ Event RetrieveUpdateDestroyAPIView """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "slug"


class BudgetListCreateView(ListCreateAPIView):
    """ Budget ListCreateAPIView """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """ Budget RetrieveUpdateDestroyAPIView """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_field = "pk"


class TransactionListCreateView(ListCreateAPIView):
    """ Transaction ListCreateAPIView """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """ Transaction RetrieveUpdateDestroyAPIView """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "pk"
