# Generated by Django 4.2.5 on 2023-12-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainWindow', '0003_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
    ]
