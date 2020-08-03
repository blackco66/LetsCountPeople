# Generated by Django 3.0.5 on 2020-08-03 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0005_review_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentpeople',
            name='gym',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Gym'),
        ),
        migrations.CreateModel(
            name='ReviewComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Review')),
            ],
        ),
    ]