# Generated by Django 4.2.4 on 2024-01-18 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='item',
            new_name='items',
        ),
    ]