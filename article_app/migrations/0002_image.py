# Generated by Django 3.2.15 on 2023-01-25 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(max_length=1000, upload_to='static/media/images')),
                ('caption', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article_app.article')),
            ],
        ),
    ]
