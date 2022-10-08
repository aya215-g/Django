# Generated by Django 4.0.3 on 2022-05-03 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCollectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200)),
                ('image_description', models.TextField()),
                ('image_time', models.DateTimeField(auto_now_add=True)),
                ('img_file', models.ImageField(upload_to='upload_images/')),
            ],
        ),
    ]