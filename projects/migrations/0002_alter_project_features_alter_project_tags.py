# Generated by Django 4.1.7 on 2023-03-16 13:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='features',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('streeet', ' From the streets to safety'), ('wish', ' I wish to feed the orangutans'), ('volunteer', 'Nemo enim ipsam voluptatem quia'), ('entity', 'single entity'), ('principle', 'Successive principle:'), ('order', 'Made to order:')], max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='project_tags', to='tags.tags'),
        ),
    ]