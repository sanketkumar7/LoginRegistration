# Generated by Django 4.2 on 2023-05-04 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('std_registration', '0004_student_unique_person'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='student',
            name='unique_person',
        ),
    ]
