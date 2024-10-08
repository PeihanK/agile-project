# Generated by Django 4.2.16 on 2024-09-05 07:46

import apps.users.choices.positions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('CEO', 'CEO'), ('CTO', 'CTO'), ('DESIGNER', 'Designer'), ('PRODUCT_OWNER', 'Product Owner'), ('PROJECT_OWNER', 'Project Owner'), ('PROGRAMMER', 'Programmer'), ('PROJECT_MANAGER', 'Project Manager'), ('QA', 'QA')], default=apps.users.choices.positions.Positions['PROGRAMMER'], max_length=15),
        ),
    ]
