# Generated by Django 3.2 on 2021-05-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20210426_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botserver',
            name='path_to_key',
            field=models.FileField(blank=True, help_text='Вставьте файл с ssh ключом', null=True, upload_to='', verbose_name='Key-File'),
        ),
        migrations.AlterField(
            model_name='botserver',
            name='ssh_key',
            field=models.TextField(blank=True, help_text='Вставьте ssh ключ', null=True, verbose_name='Key-Text'),
        ),
    ]
