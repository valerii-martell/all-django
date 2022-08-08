# Generated by Django 4.0.6 on 2022-08-08 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('platform', models.CharField(max_length=64)),
                ('year', models.DateField()),
                ('genre', models.CharField(max_length=64)),
                ('publisher', models.CharField(max_length=64)),
                ('na_sales', models.FloatField()),
                ('eu_sales', models.FloatField()),
                ('jp_sales', models.FloatField()),
                ('other_sales', models.FloatField()),
                ('global_sales', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GamerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='GamerLibraryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('game', models.ManyToManyField(to='orm.gamemodel')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orm.gamermodel')),
            ],
        ),
    ]
