# Generated by Django 4.0.2 on 2022-03-09 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0006_requestlist_amount_requestlist_comment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='requestlist',
            options={'managed': False},
        ),
    ]
