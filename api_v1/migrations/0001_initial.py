# Generated by Django 4.1.7 on 2023-05-16 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('empty_slots', models.IntegerField()),
                ('free_bikes', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.network')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.network')),
            ],
        ),
    ]