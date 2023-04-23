# Generated by Django 4.1.7 on 2023-04-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapi', '0004_rename_updated_at_user_update_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
