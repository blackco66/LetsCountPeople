# Generated by Django 3.0.5 on 2020-08-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_merge_20200806_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]