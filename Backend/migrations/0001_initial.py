# Generated by Django 5.0.4 on 2024-05-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='martdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=300, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
    ]
