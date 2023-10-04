# Generated by Django 4.2.5 on 2023-09-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_group_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='language',
            field=models.ManyToManyField(to='songs.language'),
        ),
        migrations.RemoveField(
            model_name='group',
            name='language',
        ),
        migrations.AddField(
            model_name='group',
            name='language',
            field=models.ManyToManyField(to='songs.language'),
        ),
    ]