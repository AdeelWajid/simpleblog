# Generated by Django 3.2.7 on 2021-09-22 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='theblog.category'),
            preserve_default=False,
        ),
    ]
