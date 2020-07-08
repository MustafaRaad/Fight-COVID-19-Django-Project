# Generated by Django 3.0.7 on 2020-07-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidApp', '0008_auto_20200629_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awarenesspost',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='awareness/'),
        ),
        migrations.AlterField(
            model_name='bepositivepost',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='bePositive/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='bePositive/'),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
        migrations.AlterField(
            model_name='toolspost',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='tools/'),
        ),
    ]
