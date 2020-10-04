""" URL Configuration for Main """
from django.urls import path

from .views import WalletListCreateView, WalletRetrieveUpdateAPIView

urlpatterns = [
    path(
        "wallet/",
        WalletListCreateView.as_view(),
        name="wallet_lc"
    ),
    path(
        "wallet/<str:name>/",
        WalletRetrieveUpdateAPIView.as_view(),
        name="wallet_rud"
    )
]
