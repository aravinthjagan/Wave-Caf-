# Generated by Django 5.0.4 on 2024-04-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Mail', models.CharField(default='', max_length=50)),
                ('Phone', models.IntegerField(default='')),
                ('Message', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Franchise_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Phone', models.IntegerField(default='')),
                ('Mail', models.CharField(default='', max_length=50)),
                ('City', models.CharField(default='', max_length=50)),
                ('Investment', models.IntegerField(default='')),
                ('Information', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Person', models.IntegerField(default='')),
                ('Mail', models.CharField(default='', max_length=50)),
                ('Date', models.DateField(default='')),
                ('Time', models.TimeField(default='')),
                ('Phone', models.IntegerField(default='')),
                ('Plan', models.CharField(choices=[('afternoon', 'AFTERNOON'), ('evening', 'EVENING'), ('dinner', 'DINNER')], default='afternoon', max_length=10)),
                ('Occasion', models.CharField(choices=[('anniversary', 'ANNIVERSARY'), ('birthday', 'BIRTHDAY'), ('get together', 'GET TOGETHER'), ('other', 'OTHER')], default='anniversary', max_length=20)),
                ('Special', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
