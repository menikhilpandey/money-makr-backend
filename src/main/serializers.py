from rest_framework.reverse import reverse
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
)

from .models import Wallet, Category, Event, Budget, Transaction


class WalletSerializer(HyperlinkedModelSerializer):
    """Serialize Wallet data"""

    class Meta:
        model = Wallet
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "wallet_rud",
            }
        }


class CategorySerializer(ModelSerializer):
    """Serialize Category data"""
    url = SerializerMethodField()
    sub_categories = SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_sub_categories(self, category):
        """ Get Sub Categories """
        return map(
            lambda slug: reverse(
                "category_rud",
                kwargs=dict(slug=slug),
                request=self.context["request"],
            ),
            Category.objects.filter(
                parent__slug=category.slug
            ).values_list('slug', flat=True)
        )

    def get_url(self, category):
        """Build full URL for Category detail"""
        return reverse(
            "category_rud",
            kwargs=dict(slug=category.slug),
            request=self.context["request"],
        )


class EventSerializer(HyperlinkedModelSerializer):
    """Serialize Event data"""

    class Meta:
        model = Event
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "event_rud",
            }
        }


class BudgetSerializer(HyperlinkedModelSerializer):
    """Serialize Budget data"""

    category = HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        lookup_field="slug",
        view_name="category_rud",
    )

    class Meta:
        model = Budget
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "pk",
                "view_name": "budget_rud",
            }
        }


class TransactionSerializer(HyperlinkedModelSerializer):
    """Serialize Transaction data"""

    category = HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        lookup_field="slug",
        view_name="category_rud",
    )

    wallet = HyperlinkedRelatedField(
        queryset=Wallet.objects.all(),
        lookup_field="slug",
        view_name="wallet_rud",
    )

    event = HyperlinkedRelatedField(
        queryset=Event.objects.all(),
        lookup_field="slug",
        view_name="event_rud",
        allow_null=True,
    )

    class Meta:
        model = Transaction
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "pk",
                "view_name": "transaction_rud",
            }
        }
