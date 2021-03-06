# Generated by Django 4.0.2 on 2022-02-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HardDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creationDate', models.DateField(blank=True, db_column='Creation Date', null=True)),
                ('serialNo', models.IntegerField(blank=True, db_column='Serial Number', null=True)),
                ('manufacturer', models.CharField(blank=True, db_column='Manufacturer', max_length=50, null=True)),
                ('modelNo', models.IntegerField(blank=True, db_column='Model Number', null=True)),
                ('hdType', models.CharField(blank=True, db_column=' Hard Drive Type', max_length=50, null=True)),
                ('connPort', models.CharField(blank=True, db_column=' Hard Drive Connection Port', max_length=50, null=True)),
                ('hdSize', models.CharField(blank=True, db_column='Hard Drive Size', max_length=50, null=True)),
                ('hdClass', models.CharField(blank=True, db_column=' Hard Drive Classification', max_length=50, null=True)),
                ('justiClass', models.FileField(blank=True, db_column='Justification for Classification Change', null=True, upload_to='')),
                ('imageVerID', models.IntegerField(blank=True, db_column='Image Version ID', null=True)),
                ('btStatus', models.BooleanField(blank=True, db_column='Boot Test Passed?', null=True)),
                ('btExpDate', models.DateField(blank=True, db_column='Boot Expiration Date', null=True)),
                ('hdStatus', models.CharField(blank=True, db_column='HD Status', max_length=50, null=True)),
                ('justiStatus', models.FileField(blank=True, db_column='Justification Change Status', null=True, upload_to='')),
                ('issueDate', models.DateField(blank=True, db_column='Issue Date', null=True)),
                ('expectRetDate', models.DateField(blank=True, db_column='Expected Returned Date', null=True)),
                ('justiRetDate', models.FileField(blank=True, db_column='Justification Change Return Date', null=True, upload_to='')),
                ('actualRetDate', models.DateField(blank=True, db_column='Actual Returned Date', null=True)),
                ('modDate', models.DateField(blank=True, db_column='Modified Date', null=True)),
            ],
            options={
                'db_table': 'harddrive',
                'managed': False,
            },
        ),
    ]
