# Generated by Django 3.2.4 on 2021-06-26 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('repeat', models.DateTimeField(blank=True, null=True)),
                ('state', models.CharField(choices=[('TD', 'Today'), ('IMP', 'Important'), ('P', 'Planned'), ('A', 'All'), ('C', 'Completed'), ('T', 'Tasks')], default='T', max_length=3)),
                ('add_file', models.FileField(blank=True, upload_to='')),
                ('add_step', models.CharField(blank=True, max_length=5000, null=True)),
                ('category', models.CharField(blank=True, choices=[('G', 'Green'), ('Y', 'Yellow'), ('R', 'Red')], max_length=1, null=True)),
                ('prioritize', models.CharField(blank=True, choices=[('A', 'THE_MOST_IMPORTANT'), ('B', 'IMPORTANT'), ('C', 'LESS_IMPORTANT'), ('D', 'NOT_IMPORTANT_AT_ALL')], max_length=2, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'order_with_respect_to': 'user',
            },
        ),
        migrations.CreateModel(
            name='NewList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('assigned_task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tasks.task')),
            ],
        ),
    ]
