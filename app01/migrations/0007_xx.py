# Generated by Django 3.2.9 on 2021-11-29 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='XX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='名称')),
                ('image', models.FileField(upload_to='', verbose_name='头像')),
            ],
        ),
    ]
