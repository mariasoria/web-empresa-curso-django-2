# Generated by Django 3.0.5 on 2020-04-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delegations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='Lugar')),
                ('name', models.CharField(max_length=100, verbose_name='Persona encargada')),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Delegacion',
                'verbose_name_plural': 'Delegaciones',
                'ordering': ['place'],
            },
        ),
    ]
