# Generated by Django 3.2.6 on 2021-10-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='penguin',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
    ]
