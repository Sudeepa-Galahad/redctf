# Generated by Django 2.1.5 on 2019-12-04 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=512)),
                ('points', models.IntegerField(default=0)),
                ('flag', models.CharField(max_length=100)),
                ('hosted', models.BooleanField(default=False)),
                ('imageName', models.CharField(default=None, max_length=100, null=True)),
                ('ports', models.CharField(default=None, max_length=100, null=True)),
                ('pathPrefix', models.CharField(default=None, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='categories.Category')),
            ],
        ),
    ]
