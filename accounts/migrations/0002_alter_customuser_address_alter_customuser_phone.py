# Generated by Django 4.1.3 on 2022-11-27 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.useraddress'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(db_index=True, max_length=250, null=True),
        ),
    ]
