# Generated by Django 5.0.3 on 2025-05-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='example/'),
        ),
    ]
