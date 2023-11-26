# Generated by Django 3.2 on 2023-11-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_title', models.CharField(max_length=200)),
                ('award_year', models.IntegerField()),
                ('award_info', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Awards',
                'verbose_name_plural': 'Awards',
                'ordering': ('-award_year',),
            },
        ),
    ]