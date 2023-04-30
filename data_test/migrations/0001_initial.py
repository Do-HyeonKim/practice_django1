# Generated by Django 4.1.7 on 2023-04-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_date', models.DateField(auto_now_add=True)),
                ('reg_dtm', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('uuid', models.CharField(max_length=255, null=True)),
                ('last_timestamp', models.CharField(max_length=255, null=True)),
                ('last_file_name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'dt_status',
            },
        ),
    ]