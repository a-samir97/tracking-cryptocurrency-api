# Generated by Django 3.0.7 on 2020-06-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crypto_name', models.CharField(max_length=25)),
                ('price', models.CharField(max_length=20)),
                ('market_cap', models.CharField(max_length=30)),
                ('change', models.CharField(max_length=30)),
            ],
        ),
    ]
