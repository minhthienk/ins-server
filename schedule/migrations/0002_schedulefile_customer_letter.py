# Generated by Django 3.1.7 on 2021-03-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulefile',
            name='customer_letter',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]