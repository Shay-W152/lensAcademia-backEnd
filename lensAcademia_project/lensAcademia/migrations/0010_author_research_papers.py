# Generated by Django 4.2.3 on 2023-07-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensAcademia', '0009_remove_researchpaper_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='research_papers',
            field=models.ManyToManyField(to='lensAcademia.researchpaper'),
        ),
    ]
