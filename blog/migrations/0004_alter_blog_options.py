# Generated by Django 4.1.1 on 2022-09-15 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_created_alter_blog_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id']},
        ),
    ]