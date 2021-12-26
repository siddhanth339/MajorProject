# Generated by Django 4.0 on 2021-12-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Success',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=20)),
                ('Crop', models.CharField(max_length=20)),
                ('SuccessRate', models.DecimalField(decimal_places=4, default=0.0, max_digits=12)),
            ],
        ),
    ]
