from .models import Transaction
from .serializers import TransactionSerializer
from .views import TransactionDetailView, TransactionListCreateView,BudgetView
from django.urls import path

urlpatterns = [
    path('', TransactionListCreateView.as_view(), name = 'transactions'),
    path('<int:pk>', TransactionDetailView.as_view(), name = 'transaction-details'),
    path('budget/', BudgetView.as_view(), name = 'budget')
]