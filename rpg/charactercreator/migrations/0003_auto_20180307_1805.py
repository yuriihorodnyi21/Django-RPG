# Generated by Django 2.0.2 on 2018-03-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0001_initial'),
        ('charactercreator', '0002_auto_20180306_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleric',
            name='inventory',
            field=models.ManyToManyField(to='armory.Item', verbose_name='Items the character has'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='inventory',
            field=models.ManyToManyField(to='armory.Item', verbose_name='Items the character has'),
        ),
        migrations.AddField(
            model_name='mage',
            name='inventory',
            field=models.ManyToManyField(to='armory.Item', verbose_name='Items the character has'),
        ),
        migrations.AddField(
            model_name='thief',
            name='inventory',
            field=models.ManyToManyField(to='armory.Item', verbose_name='Items the character has'),
        ),
        migrations.AlterField(
            model_name='cleric',
            name='name',
            field=models.CharField(max_length=30, verbose_name="Character's name"),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='name',
            field=models.CharField(max_length=30, verbose_name="Character's name"),
        ),
        migrations.AlterField(
            model_name='mage',
            name='name',
            field=models.CharField(max_length=30, verbose_name="Character's name"),
        ),
        migrations.AlterField(
            model_name='thief',
            name='name',
            field=models.CharField(max_length=30, verbose_name="Character's name"),
        ),
    ]