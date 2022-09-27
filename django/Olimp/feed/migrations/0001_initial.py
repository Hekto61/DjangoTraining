# Generated by Django 4.1.1 on 2022-09-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Olimp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Date_Start', models.DateTimeField(blank=True, null=True)),
                ('Date_End', models.DateTimeField(blank=True, null=True)),
                ('Site', models.URLField(null=True)),
            ],
        ),
    ]
