# Generated by Django 4.1.3 on 2022-12-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tptest2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('specialty', models.TextField()),
                ('insurance', models.TextField()),
                ('available_times1', models.TextField()),
                ('available_times2', models.TextField()),
                ('available_times3', models.TextField()),
                ('available_times4', models.TextField()),
                ('available_times5', models.TextField()),
                ('is_verified', models.BooleanField()),
                ('distance', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='tptest',
            name='distance',
            field=models.FloatField(),
        ),
    ]
