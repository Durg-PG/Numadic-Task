# Generated by Django 4.2.4 on 2023-08-02 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_open', models.DateTimeField()),
                ('harsh_acceleration', models.FloatField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('lic_plate_no', models.CharField(max_length=20)),
            ],
        ),
    ]
