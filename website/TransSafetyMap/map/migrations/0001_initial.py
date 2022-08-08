# Generated by Django 4.1 on 2022-08-08 01:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='incident',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('city', models.CharField(editable=False, max_length=128)),
                ('state', models.CharField(editable=False, max_length=2)),
                ('year', models.IntegerField(editable=False)),
                ('severity', models.CharField(editable=False, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Incidents',
            },
        ),
    ]
