# Generated by Django 4.0.2 on 2022-04-19 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0006_requestlist_amount_requestlist_comment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestlist',
            options={'managed': False},
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
