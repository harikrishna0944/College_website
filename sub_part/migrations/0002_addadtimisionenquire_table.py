# Generated by Django 4.0.5 on 2022-07-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addadtimisionenquire_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('enquirydate', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('DOB', models.CharField(max_length=100)),
                ('Departments', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
