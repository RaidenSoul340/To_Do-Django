# Generated by Django 5.1.2 on 2024-10-29 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomeF', models.CharField(max_length=80)),
                ('funcao', models.TextField(blank=True, null=True)),
                ('presente', models.BooleanField(default=False)),
                ('hora', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
