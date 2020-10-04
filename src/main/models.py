from django.db.models import (
    FloatField,
    CharField,
    BooleanField,
    DateTimeField,
    Model,
    ForeignKey,
    CASCADE,
)


class Wallet(Model):
    """ Wallet Model """
    name = CharField(max_length=63)
    wallet_type = CharField(
        max_length=63,
        default='liquid_assets'
    )
    currency = CharField(max_length=7)
    balance = FloatField(default=0)
    exclude_from_total = BooleanField(default=False)
    isActive = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("name", "wallet_type")

    def __str__(self):
        return self.name + self.wallet_type + self.balance


class Category(Model):
    name = CharField(max_length=63, primary_key=True)
    parent = ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=CASCADE,
    )
    isActive = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'spending category'
