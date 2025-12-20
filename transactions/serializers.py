from rest_framework import serializers
from .models import Transaction
from categories.models import Category


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'category',
            'type',
            'amount',
            'date',
            'description',
        ]

    def validate_amount(self, value):
        if value <=0:
            raise serializers.ValidationError(
                "Transaction amount must be greater than zero."

            )
        return value

    def validate_category(self, value):
        user = self.context['request'].user
        if value.user != user:
            raise serializers.ValidationError(
                "You can only use your own categories"
            )
        return value


