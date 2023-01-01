# Generated by Django 4.1.3 on 2022-12-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_donator'),
        ('accounts', '0004_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mass_fundraise',
            field=models.ManyToManyField(blank=True, related_name='fundraised_books', to='books.book'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='obtained',
            field=models.ManyToManyField(blank=True, related_name='obtained_books', to='books.book'),
        ),
    ]