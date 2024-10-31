# Generated by Django 5.1.2 on 2024-10-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rating', models.CharField(choices=[(' ⭐ ', ' ⭐ '), (' ⭐ ⭐ ', ' ⭐ ⭐ '), (' ⭐ ⭐ ⭐ ', ' ⭐ ⭐ ⭐ '), (' ⭐ ⭐ ⭐ ⭐ ', ' ⭐ ⭐ ⭐ ⭐ '), (' ⭐ ⭐ ⭐ ⭐ ⭐ ', ' ⭐ ⭐ ⭐ ⭐ ⭐ ')], max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]