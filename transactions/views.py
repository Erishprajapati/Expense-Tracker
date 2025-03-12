from django.shortcuts import render
from .serializers import TransactionSerializer, BudgetSerializer
from rest_framework import generics, permissions
from .models import Transaction, Budget

# Create your views here.
class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save (user= self.request.user)

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Transaction.objects.filter(user = self.request.user)
    


class BudgetView(generics.RetrieveUpdateAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.all(user = self.request.user)