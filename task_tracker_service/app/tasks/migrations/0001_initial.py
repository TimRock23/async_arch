# Generated by Django 5.0.2 on 2024-03-02 21:36

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


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
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='уникальный идентификатор')),
                ('name', models.CharField(max_length=512, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('status', models.CharField(choices=[('OPEN', 'Открыта'), ('DONE', 'Выполнена')], default='OPEN', max_length=64, verbose_name='статус')),
                ('assignee', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL, verbose_name='исполнитель')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
            },
        ),
    ]
