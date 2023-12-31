# Generated by Django 4.2.4 on 2023-11-03 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('genericbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.genericbasemodel')),
            ],
            options={
                'verbose_name': 'Class',
            },
            bases=('base.genericbasemodel',),
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('grade', models.CharField(max_length=4)),
                ('name', models.CharField(default='Average', max_length=4)),
                ('score', models.IntegerField(default=50)),
            ],
            options={
                'verbose_name': 'Grade',
            },
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='JointStudentSubjectClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('Fees', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Arrears', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
            options={
                'verbose_name': 'Student',
            },
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='StudentScore',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
            ],
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('genericbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.genericbasemodel')),
            ],
            options={
                'verbose_name': 'Subject',
            },
            bases=('base.genericbasemodel',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
            ],
            options={
                'verbose_name': 'Teacher',
            },
            bases=('base.basemodel',),
        ),
    ]
