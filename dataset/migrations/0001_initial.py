# Generated by Django 4.1.5 on 2023-09-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('tanggal', models.DateField()),
                ('qty', models.IntegerField()),
                ('nilai', models.IntegerField()),
            ],
        ),
    ]
