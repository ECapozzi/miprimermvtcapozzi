# Generated by Django 4.1 on 2022-08-24 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appFamilia", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="familiar", old_name="parentezco", new_name="parentesco",
        ),
    ]
