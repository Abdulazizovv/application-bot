# Generated by Django 5.0.1 on 2025-03-05 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('botapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('about', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('new', 'Yangi'), ('in_progress', 'Jarayonda'), ('accepted', 'Tasdiqlandi'), ('rejected', 'Rad etildi')], default='new', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='botapp.botuser')),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
                'ordering': ['-created_at'],
            },
        ),
    ]
