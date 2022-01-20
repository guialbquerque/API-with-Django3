# Generated by Django 4.0.1 on 2022-01-20 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('B', 'Basic'), ('I', 'Intermediate'), ('A', 'Advanced')], default='B', max_length=1),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_course', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternonn'), ('N', 'Nocturne')], default='M', max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
    ]
