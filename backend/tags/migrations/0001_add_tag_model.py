# Generated by Django 3.2.16 on 2024-05-14 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('#008000', 'Зеленый'), ('#FFA500', 'Оранжевый'), ('#FF0000', 'Красный')], max_length=10, unique=True, verbose_name='Цвет')),
                ('name', models.CharField(choices=[('Завтрак', 'Завтрак'), ('Обед', 'Обед'), ('Ужин', 'Ужин')], max_length=10, unique=True, verbose_name='Тег')),
                ('slug', models.SlugField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=10, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
    ]
