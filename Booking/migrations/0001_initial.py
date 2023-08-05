# Generated by Django 3.2.20 on 2023-08-05 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('date_time', models.DateTimeField()),
                ('table_count', models.PositiveIntegerField(default=1)),
                ('is_canceled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appetizer', models.CharField(max_length=100)),
                ('main_course', models.CharField(max_length=100)),
                ('dessert', models.CharField(max_length=100)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Booking.booking')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.venue'),
        ),
    ]