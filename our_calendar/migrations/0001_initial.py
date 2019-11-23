from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('level', models.CharField(choices=[('Po prostu kod', 'Po prostu kod'), ('Dokumentacja i kod', 'Dokumentacja i kod'), ('Krew, Stack Overflow i łzy', 'Krew, Stack Overflow i łzy'), ('Droga ku depresji', 'Droga ku depresji')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('file', models.FileField(blank=True, null=True, upload_to='answers/%Y/%m/%d/')),
                ('url', models.URLField(blank=True, null=True)),
                ('is_checked', models.BooleanField(default=False)),
                ('is_correct', models.BooleanField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='our_calendar.Task')),
            ],
        ),
        migrations.AddConstraint(
            model_name='answer',
            constraint=models.UniqueConstraint(fields=('email', 'task'), name='unique key'),
        ),
    ]
