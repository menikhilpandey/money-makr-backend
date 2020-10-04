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


class Wallet(Model):
    """ Wallet Model: CRU """
    name = CharField(max_length=63, primary_key=True)
    wallet_type = CharField(
        max_length=63,
        default='liquid_assets'
    )
    currency = CharField(max_length=7)
    balance = FloatField(default=0)
    exclude_from_total = BooleanField(default=False)

    def __str__(self):
        return self.name + self.wallet_type + str(self.balance)

    def delete(self, *args, **kwargs):
        return


class Category(Model):
    """ Category Model: CRU """
    name = CharField(
        max_length=63,
        primary_key=True,
        default='Others'
    )
    parent = ForeignKey(
        'self',
        null=True,
        related_name='sub_category',
        on_delete=SET_NULL,
    )

    class Meta:
        verbose_name = 'spending category'

    def __str__(self):
        return self.parent.name + self.name

    def delete(self, *args, **kwargs):
        return


class Event(Model):
    """ Event Model: CRUD"""
    name = CharField(max_length=63)
    budget_goal = FloatField(default=0)

    def __str__(self):
        return str(self.name)


class Budget(Model):
    """ Event Model: CRUD"""
    category = ForeignKey(
        Category,
        default='All',
        on_delete=CASCADE
    )
    budget_goal = FloatField(default=0)
    start_date = DateField(null=True)
    end_date = DateField(null=True)

    def __str__(self):
        return str(self.category) + str(self.budget_goal)


class Transaction(Model):
    """ Event Model: CRUD"""
    amount = FloatField(default=0)
    category = ForeignKey(
        Category,
        default='Others',
        on_delete=SET_DEFAULT
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
