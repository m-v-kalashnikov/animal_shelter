# Generated by Django 2.2.6 on 2019-12-07 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal_shelter', '0004_auto_20191206_0650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_of_animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='animal',
            name='type_of_animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal_shelter.Type_of_animal'),
        ),
    ]
