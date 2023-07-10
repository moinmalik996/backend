# Generated by Django 4.2.3 on 2023-07-10 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_adslocation_visits_alter_adslocation_max_visits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='adslocation',
            name='max_visits',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='adslocation',
            name='visits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]