# Generated by Django 4.2.3 on 2023-07-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homewrk_02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='reg_date',
            field=models.DateField(),
        ),
    ]