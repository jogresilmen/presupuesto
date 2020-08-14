# Generated by Django 2.2.7 on 2019-11-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('prefix', models.CharField(default='default', max_length=40, verbose_name='Prefix')),
                ('padding', models.PositiveIntegerField(default=4, verbose_name='padding')),
                ('initial', models.PositiveIntegerField(default=1, verbose_name='initial')),
                ('increment', models.PositiveIntegerField(default=1, verbose_name='increment')),
                ('reset', models.PositiveIntegerField(blank=True, null=True, verbose_name='reset')),
                ('last', models.PositiveIntegerField(editable=False, verbose_name='Last')),
                ('next_val', models.PositiveIntegerField(verbose_name='Next')),
            ],
            options={
                'verbose_name': 'sequence',
                'verbose_name_plural': 'sequences',
            },
        ),
        migrations.DeleteModel(
            name='Clado',
        ),
        migrations.DeleteModel(
            name='Taxonomy',
        ),
    ]