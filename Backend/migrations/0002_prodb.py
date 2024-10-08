# Generated by Django 5.0.4 on 2024-05-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prodb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CatName', models.CharField(blank=True, max_length=50, null=True)),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('IImage', models.ImageField(blank=True, null=True, upload_to='media')),
                ('Description', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
