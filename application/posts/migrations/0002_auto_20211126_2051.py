# Generated by Django 3.2.9 on 2021-11-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='someposts',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Post'},
        ),
        migrations.AlterField(
            model_name='someposts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
