# Generated by Django 3.2.7 on 2021-09-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210925_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(auto_now=True),
        ),
    ]
