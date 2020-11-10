# Generated by Django 3.0.4 on 2020-11-10 16:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskDay', models.IntegerField(default=0, verbose_name='day of task')),
                ('taskDate', models.DateField(default=django.utils.timezone.now, verbose_name='date of task')),
                ('level', models.CharField(choices=[('Po prostu kod', 'Po prostu kod'), ('Dokumentacja i kod', 'Dokumentacja i kod'), ('Krew, Stack Overflow i łzy', 'Krew, Stack Overflow i łzy'), ('Droga ku depresji', 'Droga ku depresji')], default='Po prostu kod', max_length=31)),
                ('taskContent', models.TextField(default='Some good stuff for user')),
                ('category', models.CharField(default='JavaScript', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAnswer', models.TextField(default='None')),
                ('date', models.DateField(auto_now_add=True)),
                ('taskId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='our_calendar.Task')),
            ],
        ),
        migrations.CreateModel(
            name='CorrectAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correctAnswer', models.TextField(default='Some good stuff')),
                ('taskId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='our_calendar.Task')),
            ],
        ),
    ]
