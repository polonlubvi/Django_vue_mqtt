# Generated by Django 2.2 on 2019-04-12 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automation',
            fields=[
                ('automation_id', models.AutoField(primary_key=True, serialize=False)),
                ('automation_heading', models.CharField(max_length=250)),
                ('automation_body', models.TextField()),
            ],
        ),
    ]