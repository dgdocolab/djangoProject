# Generated by Django 4.2.5 on 2023-09-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_update_at_choice_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
