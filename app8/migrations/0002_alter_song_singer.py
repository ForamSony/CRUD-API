# Generated by Django 5.0.2 on 2024-03-11 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app8', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sungby', to='app8.singer'),
        ),
    ]