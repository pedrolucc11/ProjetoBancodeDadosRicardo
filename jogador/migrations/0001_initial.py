# Generated by Django 4.2.7 on 2023-12-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Jogador', max_length=200)),
                ('posicao', models.CharField(help_text='Posição', max_length=50)),
                ('num', models.CharField(help_text='Número de Preferência', max_length=2)),
            ],
        ),
    ]
