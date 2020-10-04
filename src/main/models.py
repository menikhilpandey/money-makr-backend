from django.db.models import (
    FloatField,
    CharField,
    BooleanField,
    DateField,
    TextField,
    Model,
    ForeignKey,
    SET_DEFAULT,
    SET_NULL,
    CASCADE
)

from django_extensions.db.fields import AutoSlugField


class Wallet(Model):
    """ Wallet Model """
    name = CharField(max_length=63)
    wallet_type = CharField(
        max_length=63,
        default='liquid_assets',
    )
    slug = AutoSlugField(
        max_length=127,
        populate_from=["name", "wallet_type"],
        db_index=True,
    )
    currency = CharField(max_length=7)
    balance = FloatField(default=0)
    exclude_from_total = BooleanField(default=False)

    class Meta:
        unique_together = ["name", "wallet_type"]

    def __str__(self):
        return str(self.slug)

    def delete(self, *args, **kwargs):
        return


class Category(Model):
    """ Category Model """
    name = CharField(
        max_length=63,
        default='Others',
        unique=True,
    )
    parent = ForeignKey(
        'self',
        null=True,
        related_name='sub_category',
        on_delete=SET_NULL,
    )
    slug = AutoSlugField(
        max_length=127,
        populate_from=["name"],
        db_index=True,
    )

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        return


class Event(Model):
    """ Event Model """
    name = CharField(max_length=63, unique=True)
    budget_goal = FloatField(default=0)
    slug = AutoSlugField(
        max_length=127,
        populate_from=["name"],
        db_index=True,
    )

    def __str__(self):
        return str(self.name)


class Budget(Model):
    """ Event Model """
    category = ForeignKey(
        Category,
        default='Others',
        on_delete=SET_DEFAULT,
    )
    budget_goal = FloatField(default=0)
    start_date = DateField(null=True)
    end_date = DateField(null=True)

    def __str__(self):
        return str(self.category) + str(self.budget_goal)


class Transaction(Model):
    """ Event Model"""
    amount = FloatField(default=0)
    category = ForeignKey(
        Category,
        default='Others',
        on_delete=SET_DEFAULT,
    )
    description = TextField(null=True, blank=True)
    date = DateField()
    wallet = ForeignKey(Wallet, on_delete=CASCADE)
    event = ForeignKey(Event, null=True, on_delete=SET_NULL)
    exclude_from_report = BooleanField(default=False)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return str(self.category) + str(self.wallet) + str(self.amount)
