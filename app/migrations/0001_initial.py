# Generated by Django 2.0 on 2020-05-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键自增')),
                ('username', models.CharField(max_length=12, verbose_name='用户名')),
                ('password', models.CharField(max_length=36, verbose_name='密码')),
            ],
            options={
                'db_table': 'UserProfile',
            },
        ),
    ]
