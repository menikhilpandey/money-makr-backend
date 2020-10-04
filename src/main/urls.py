""" URL Configuration for Main """
from django.urls import path

from .views import (
    WalletListCreateView,
    WalletRetrieveUpdateAPIView,
    CategoryListCreateView,
    CategoryRetrieveUpdateAPIView,
    EventListCreateView,
    EventRetrieveUpdateAPIView,
    BudgetListCreateView,
    BudgetRetrieveUpdateAPIView,
    TransactionListCreateView,
    TransactionRetrieveUpdateAPIView,
)

urlpatterns = [
    path(
        "wallet/",
        WalletListCreateView.as_view(),
        name="wallet_lc"
    ),
    path(
        "wallet/<str:slug>/",
        WalletRetrieveUpdateAPIView.as_view(),
        name="wallet_rud"
    ),
    path(
        "category/",
        CategoryListCreateView.as_view(),
        name="category_lc"
    ),
    path(
        "category/<str:slug>/",
        CategoryRetrieveUpdateAPIView.as_view(),
        name="category_rud"
    ),
    path(
        "event/",
        EventListCreateView.as_view(),
        name="event_lc"
    ),
    path(
        "event/<str:slug>/",
        EventRetrieveUpdateAPIView.as_view(),
        name="event_rud"
    ),
    path(
        "budget/",
        BudgetListCreateView.as_view(),
        name="budget_lc"
    ),
    path(
        "budget/<int:pk>/",
        BudgetRetrieveUpdateAPIView.as_view(),
        name="budget_rud"
    ),
    path(
        "transaction/",
        TransactionListCreateView.as_view(),
        name="transaction_lc"
    ),
    path(
        "transaction/<int:pk>/",
        TransactionRetrieveUpdateAPIView.as_view(),
        name="transaction_rud"
    ),
]
