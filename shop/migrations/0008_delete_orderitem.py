# Generated by Django 5.0.3 on 2024-04-26 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_orderitem_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
