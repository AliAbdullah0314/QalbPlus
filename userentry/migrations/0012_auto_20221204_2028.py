# Generated by Django 3.1 on 2022-12-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userentry', '0011_auto_20221204_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='endtime',
            field=models.CharField(blank=True, choices=[('9:30', '9:30'), ('10', '10'), ('10:30', '10:30'), ('11', '11'), ('11:30', '11:30'), ('12', '12'), ('12:30', '12:30'), ('13', '13'), ('13:30', '13:30'), ('14', '14')], default='9', max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='insuranceaccepted',
            field=models.CharField(blank=True, choices=[('OIC', 'OIC'), ('oman', 'Oman'), ('xyz', 'yxz')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='insurancedetails',
            field=models.CharField(blank=True, choices=[('OIC', 'OIC'), ('oman', 'Oman'), ('xyz', 'yxz')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='specialty',
            field=models.CharField(blank=True, choices=[('GP', 'GP'), ('Dentist', 'Dentist'), ('opt', 'Ophthalmologist'), ('ent', 'ENT')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='starttime',
            field=models.CharField(blank=True, choices=[('9:00', '9:00'), ('9:30', '9:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00')], default='9', max_length=5),
        ),
    ]
