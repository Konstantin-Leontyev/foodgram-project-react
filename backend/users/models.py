from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField

from .constants import NAME_FIELDS_MAX_LENGTH
from .validators import me_value_username_validator, unicode_username_validator


class User(AbstractUser):
    """Describes user model."""

    email = EmailField(
        verbose_name='Адрес электронной почты',
        unique=True
    )
    first_name = CharField(
        verbose_name='Имя',
        max_length=NAME_FIELDS_MAX_LENGTH
    )
    last_name = CharField(
        verbose_name='Фамилия',
        max_length=NAME_FIELDS_MAX_LENGTH
    )
    username = CharField(
        verbose_name='Имя пользователя',
        max_length=NAME_FIELDS_MAX_LENGTH,
        unique=True,
        validators=[
            me_value_username_validator,
            unicode_username_validator,
        ]
    )

    REQUIRED_FIELDS = [
        'first_name',
        'id',
        'last_name',
        'username',
    ]

    USERNAME_FIELD = 'email'

    class Meta:
        default_related_name = 'users'
        ordering = ('username', 'email')
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __repr__(self):
        """Returns text representation of the class."""
        return self.get_full_name()
