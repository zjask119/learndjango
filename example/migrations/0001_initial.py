# Generated by Django 2.2 on 2019-09-28 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('released', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('viewed', models.BooleanField(default=False)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='example.Genre')),
            ],
        ),
    ]
