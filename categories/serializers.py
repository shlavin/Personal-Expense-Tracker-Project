from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Category name cannot be empty.")

        if len(value) > 100:
            raise serializers.ValidationError(
                "Category name must be less than 100 characters."
            )

        user = self.context['request'].user
        if Category.objects.filter(user=user, name=value).exists():
            raise serializers.ValidationError(
                "You already have a category with this name."
            )

        return value

    