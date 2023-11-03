# Generated by Django 4.2.4 on 2023-11-03 08:07

import base.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpinSchoolUsers',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], default='OTHER', max_length=10)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('state', models.ForeignKey(default=base.models.State.default_state, on_delete=django.db.models.deletion.CASCADE, to='base.state')),
            ],
            options={
                'verbose_name': 'SpinSchoolUser',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
