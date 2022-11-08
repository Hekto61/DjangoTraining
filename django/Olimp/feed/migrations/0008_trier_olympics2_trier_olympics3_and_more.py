# Generated by Django 4.1.1 on 2022-11-08 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_rename_olympics_trier_olympics1'),
    ]

    operations = [
        migrations.AddField(
            model_name='trier',
            name='Olympics2',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='Olympics2', to='feed.olimp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trier',
            name='Olympics3',
            field=models.ForeignKey(default=321, on_delete=django.db.models.deletion.CASCADE, related_name='Olympics3', to='feed.olimp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trier',
            name='Olympics1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='First_olimp', to='feed.olimp'),
        ),
    ]