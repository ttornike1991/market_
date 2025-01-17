# Generated by Django 4.1.7 on 2023-02-25 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(default='', help_text='Enter your first name', max_length=50)),
                ('l_name', models.CharField(default='', help_text='Enter your first name', max_length=50)),
                ('birth_date', models.DateField(default=django.utils.timezone.now, help_text='Enter your birth date')),
                ('is_valide', models.BooleanField(default=False)),
                ('email', models.EmailField(help_text='Enter your email address', max_length=254, unique=True)),
            ],
        ),
    ]
