# Generated by Django 4.1.7 on 2023-10-10 15:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField(unique_for_year=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='years',
        ),
        migrations.RemoveField(
            model_name='song',
            name='years',
        ),
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='group',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(upload_to='albums/'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(upload_to='groups/'),
        ),
        migrations.RemoveField(
            model_name='group',
            name='language',
        ),
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='songs.year'),
        ),
        migrations.AddField(
            model_name='group',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='songs.character'),
        ),
        migrations.AddField(
            model_name='song',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='songs.character'),
        ),
        migrations.AddField(
            model_name='group',
            name='language',
            field=models.ManyToManyField(to='songs.language'),
        ),
        migrations.AlterField(
            model_name='group',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='songs.year'),
        ),
    ]