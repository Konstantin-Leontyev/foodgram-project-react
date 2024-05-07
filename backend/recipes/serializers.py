from django.db.models import F
from django.db.transaction import atomic
from drf_extra_fields.fields import Base64ImageField
from ingredients.models import Ingredient
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from tags.serializers import TagSerializer
from users.serializers import CustomUserSerializer

from .models import Recipe, RecipeIngredient


class RecipeSerializer(ModelSerializer):
    """Describes Recipe serializer class."""

    image = Base64ImageField()
    tags = TagSerializer(many=True, read_only=True)
    author = CustomUserSerializer(read_only=True)
    ingredients = SerializerMethodField()
    is_favorited = SerializerMethodField()
    is_in_shopping_cart = SerializerMethodField()

    class Meta:
        """Describes Recipe serializer metaclass."""

        model = Recipe
        fields = '__all__'
        read_only_fields = ['is_favorited', 'is_in_shopping_cart']

    def get_ingredients(self, obj):
        """Ingredients get function."""
        ingredients = obj.ingredients.values(
            'id', 'name', 'measurement_unit', amount=F('ingredient__amount')
        )
        return ingredients

    def get_is_favorited(self, obj):
        return False

    def get_is_in_shopping_cart(self, obj):
        return False

    def create_ingredients(self, ingredients, recipe):
        for i in ingredients:
            ingredient = Ingredient.objects.get(id=i['id'])
            RecipeIngredient.objects.create(
                ingredients=ingredient,
                recipe=recipe,
                amount=i['amount']
            )

    @atomic
    def create(self, validated_data):
        author = self.context.get('request').user
        validated_data.update({'author': author})

        tags = self.initial_data.pop('tags')
        ingredients = self.initial_data.pop('ingredients')

        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags)
        self.create_ingredients(ingredients, recipe)
        return recipe
