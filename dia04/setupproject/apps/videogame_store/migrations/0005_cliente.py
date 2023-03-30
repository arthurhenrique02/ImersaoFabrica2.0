# Generated by Django 4.1.7 on 2023-03-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogame_store', '0004_alter_jogo_ano'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do cliente', max_length=100)),
                ('endereco', models.CharField(help_text='Endereço do cliente', max_length=100)),
                ('telefone', models.CharField(help_text='Telefone para contato do cliente', max_length=20)),
            ],
        ),
    ]
