# Generated by Django 5.1.3 on 2025-01-14 16:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoques', '0005_estoque_valor_unitario'),
    ]

    operations = [
        migrations.AddField(
            model_name='provisao',
            name='data_para_entregar',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
