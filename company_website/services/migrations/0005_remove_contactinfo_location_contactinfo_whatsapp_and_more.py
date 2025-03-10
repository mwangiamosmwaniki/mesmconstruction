# Generated by Django 4.2.16 on 2025-02-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_remove_servicecategory_image_remove_siteimage_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='location',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='whatsapp',
            field=models.CharField(default='+254700123456', max_length=15),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(default='+254700123456', max_length=15),
        ),
    ]
