# Generated by Django 4.0.3 on 2022-05-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dep_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
