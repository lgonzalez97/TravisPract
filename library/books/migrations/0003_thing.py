# Generated by Django 4.0.3 on 2022-04-14 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_editorial_genre_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('image', models.BinaryField()),
            ],
        ),
    ]
