# Generated by Django 3.2.4 on 2022-01-12 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cost_per_item', models.IntegerField()),
                ('stock_quantity', models.IntegerField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
