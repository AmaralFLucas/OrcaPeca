# Generated by Django 5.0.5 on 2024-06-20 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcaPecas', '0007_alter_orcamento_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
