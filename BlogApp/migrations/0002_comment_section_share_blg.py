# Generated by Django 3.2.15 on 2023-09-13 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_section',
            fields=[
                ('comnt_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=200, null=True)),
                ('comment', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Share_blg',
            fields=[
                ('share_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_mail', models.CharField(max_length=200, null=True)),
                ('sender_name', models.CharField(max_length=200, null=True)),
                ('content', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]