# Generated by Django 4.1.7 on 2023-03-12 13:37

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_enum.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_commit', to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='ReportProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', django_enum.fields.EnumCharField(blank=True, choices=[('V0', 'in'), ('V1', 'Value 1'), ('V2', 'Value 2')], max_length=2, null=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_comment', to='comments.comments')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comments')),
            ],
        ),
    ]