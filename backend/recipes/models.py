from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (CASCADE, SET_NULL, CharField, ForeignKey,
                              ImageField, ManyToManyField, Model,
                              PositiveSmallIntegerField, TextField,
                              UniqueConstraint)

from core.constants import (MAX_COOKING_TIME, MAX_INGREDIENT_AMOUNT,
                            MIN_COOKING_TIME, MIN_INGREDIENT_AMOUNT,
                            NAME_FIELD_MAX_LENGTH)
from ingredients.models import Ingredient
from tags.models import Tag

User = get_user_model()


class Recipe(Model):
    """Describes recipe model class."""

    author = ForeignKey(
        User,
        null=True,
        on_delete=SET_NULL,
        verbose_name='Автор',
    )
    cooking_time = PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                limit_value=MIN_COOKING_TIME,
                message='Минимальное время приготовления '
                        f'{MIN_COOKING_TIME} мин.'
            ),
            MaxValueValidator(
                limit_value=MAX_COOKING_TIME,
                message='Максимальное время приготовления '
                        f'{MAX_COOKING_TIME} мин.'
            ),
        ],
        verbose_name='Время приготовления',
    )
    image = ImageField(
        upload_to='images/',
        verbose_name='Изображение',
    )
    ingredients = ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиенты',
    )
    name = CharField(
        max_length=NAME_FIELD_MAX_LENGTH,
        verbose_name='Название',
    )
    tags = ManyToManyField(
        Tag,
        verbose_name='Теги',
    )
    text = TextField(
        verbose_name='Описание',
    )

    class Meta:
        """Describes follow model metaclass."""

        ordering = ['-id']
        default_related_name = 'recipes'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

        def __str__(self):
            return self.name


class RecipeIngredient(Model):
    """Describes recipe ingredient model class."""

    amount = PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                limit_value=MIN_INGREDIENT_AMOUNT,
                message='Минимальное количество ингредиентов '
                        f'{MIN_INGREDIENT_AMOUNT}.'
            ),
            MaxValueValidator(
                limit_value=MAX_COOKING_TIME,
                message='Максимальное количество ингредиентов '
                        f'{MAX_INGREDIENT_AMOUNT}.'
            ),
        ],
        verbose_name="Количество",
    )
    ingredients = ForeignKey(
        Ingredient,
        on_delete=CASCADE,
        related_name='ingredient',
        verbose_name='Ингредиенты',
    )
    recipe = ForeignKey(
        Recipe,
        on_delete=CASCADE,
        related_name='recipe',
        verbose_name='Рецепты',
    )

    class Meta:
        """Describes recipe ingredient model metaclass."""

        constraints = [
            UniqueConstraint(
                fields=['ingredients', 'recipe'],
                name='Ингредиенты в рамках одного рецепта'
                     'должны быть уникальны.'
                     'Объедините ингредиенты и повторите попытку.'
            ),
        ]
        verbose_name = 'Список ингредиентов рецепта'
        verbose_name_plural = 'Список ингредиентов рецепта'
