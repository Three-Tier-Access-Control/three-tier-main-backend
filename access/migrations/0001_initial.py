# Generated by Django 4.0.4 on 2022-06-06 19:47

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('direction', models.CharField(choices=[('in', 'IN'), ('out', 'OUT')], default='in', max_length=254)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='access_logs', to='employees.employee')),
            ],
            options={
                'verbose_name': 'Access Log',
                'verbose_name_plural': 'Access Logs',
                'ordering': ('-created',),
            },
        ),
    ]
