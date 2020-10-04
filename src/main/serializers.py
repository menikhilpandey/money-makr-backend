from rest_framework.serializers import ModelSerializer

from .models import Wallet, Category, Event, Budget, Transaction


class WalletSerializer(ModelSerializer):
    """Serialize Wallet data"""

    class Meta:
        model = Wallet
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    """Serialize Category data"""

    class Meta:
        model = Category
        fields = "__all__"


class EventSerializer(ModelSerializer):
    """Serialize Event data"""

    class Meta:
        model = Event
        fields = "__all__"


class BudgetSerializer(ModelSerializer):
    """Serialize Budget data"""

    class Meta:
        model = Budget
        fields = "__all__"


class TransactionSerializer(ModelSerializer):
    """Serialize Transaction data"""

    class Meta:
        model = Transaction
        fields = "__all__"
