# Generated by Django 4.2.2 on 2024-11-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailingattempt",
            name="send_time",
            field=models.DateTimeField(verbose_name="Время отправки"),
        ),
    ]