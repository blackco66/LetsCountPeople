# Generated by Django 3.0.7 on 2020-08-03 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_review_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentpeople',
            name='gym',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Gym'),
        ),
    ]