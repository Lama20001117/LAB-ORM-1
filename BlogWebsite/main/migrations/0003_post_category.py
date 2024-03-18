# Generated by Django 5.0.2 on 2024-03-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_poster_alter_post_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Tech', 'Tech'), ('Science', 'Science'), ('Fashoin', 'Fashoin'), ('Food', 'Food')], default='General', max_length=64),
            preserve_default=False,
        ),
    ]