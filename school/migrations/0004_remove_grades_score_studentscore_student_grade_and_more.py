# Generated by Django 4.2.4 on 2023-11-03 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_grades_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grades',
            name='score',
        ),
        migrations.AddField(
            model_name='studentscore',
            name='student_grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.grades'),
        ),
        migrations.AlterField(
            model_name='studentscore',
            name='score',
            field=models.IntegerField(default=50),
        ),
    ]
