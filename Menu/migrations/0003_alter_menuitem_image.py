# Generated by Django 5.0.7 on 2025-03-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
