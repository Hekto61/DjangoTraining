# Generated by Django 4.1.1 on 2022-10-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_trier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trier',
            name='Fomka',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
