# Generated by Django 3.2 on 2022-06-01 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profile_livestyle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='livestyle',
            new_name='lifestyle',
        ),
        migrations.AlterField(
            model_name='profile',
            name='task',
            field=models.CharField(choices=[('get slim', 'get slim'), ('get save', 'get save'), ('get save', 'get grow')], max_length=10, null=True),
        ),
    ]