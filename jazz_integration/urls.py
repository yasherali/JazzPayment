from django.urls import path
from .views import JazzCashReturnView

urlpatterns = [
    path('payment/return/', JazzCashReturnView.as_view(), name='jazzcash_return'),
]