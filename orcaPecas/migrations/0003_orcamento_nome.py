# Generated by Django 5.0.5 on 2024-05-30 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcaPecas', '0002_alter_orcamento_itens_orcamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
    ]