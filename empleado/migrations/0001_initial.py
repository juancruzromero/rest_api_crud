# Generated by Django 3.0.5 on 2020-05-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('legajo', models.CharField(max_length=4)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
    ]
