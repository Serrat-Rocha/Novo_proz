# Generated by Django 4.2.20 on 2025-04-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoques', '0009_delete_usuario_remove_profile_gerente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='raridade',
            field=models.CharField(choices=[('E', 'E'), ('C', 'C'), ('B', 'B'), ('A', 'A'), ('S', 'S')], default='comum', max_length=50),
        ),
    ]
