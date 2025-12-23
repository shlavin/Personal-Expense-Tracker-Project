from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from transactions.models import Transaction


class MonthlyReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        if not year or not month:
            return Response(
                {"error": "year and month query parameters are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        transactions = Transaction.objects.filter(
            user=user,
            date__year=year,
            date__month=month
        )

        income = transactions.filter(type='income').aggregate(
            total=Sum('amount')
        )['total'] or 0

        expense = transactions.filter(type='expense').aggregate(
            total=Sum('amount')
        )['total'] or 0

        balance = income - expense

        return Response({
            "year": int(year),
            "month": int(month),
            "total_income": income,
            "total_expense": expense,
            "balance": balance
        })


