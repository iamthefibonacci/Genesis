# Generated by Django 4.0.1 on 2022-01-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_options_alter_course_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='outcome',
            field=models.TextField(null=True),
        ),
    ]
