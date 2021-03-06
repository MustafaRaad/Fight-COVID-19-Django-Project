# Generated by Django 3.0.7 on 2020-06-15 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidApp', '0005_auto_20200615_0448'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToolsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Masks', 'اقنعة'), ('Sterilizers', 'معقمات'), ('Gloves', 'كفوف'), ('Recomended', 'الموصى بها')], max_length=128)),
                ('title', models.CharField(max_length=256, unique=True)),
                ('content', models.TextField(default=' ')),
                ('img', models.ImageField(upload_to='tools_imgs/')),
            ],
        ),
        migrations.AlterField(
            model_name='newspost',
            name='img',
            field=models.ImageField(upload_to='news_imgs/'),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='title',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
