# Generated by Django 4.0.6 on 2024-05-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_resume_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
