# Generated by Django 4.1.3 on 2022-12-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armss', '0003_rename_tptest2_tptestnew'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpemail', models.TextField()),
                ('tpname', models.TextField()),
                ('patientemail', models.TextField()),
                ('patientname', models.TextField()),
                ('time', models.TextField()),
                ('day', models.TextField()),
            ],
        ),
    ]
