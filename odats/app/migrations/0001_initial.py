# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-01 01:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=200, verbose_name='Doctor Name')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('phone', models.CharField(max_length=200, verbose_name='Contact Number')),
                ('email', models.CharField(max_length=200, verbose_name='E-mail')),
                ('username', models.CharField(max_length=200, verbose_name='Username')),
                ('password', models.CharField(max_length=200, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorRequestOrgan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patientname', models.CharField(max_length=200)),
                ('Patienttype', models.CharField(max_length=200)),
                ('Bloodgroup', models.CharField(max_length=200)),
                ('Reason', models.CharField(max_length=300)),
                ('Description', models.CharField(max_length=500)),
                ('Contactnumber', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='app.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DonationReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=500)),
                ('District', models.CharField(max_length=200)),
                ('Pincode', models.CharField(max_length=200)),
                ('State', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('Blood_group', models.CharField(max_length=200)),
                ('Relative_name', models.CharField(max_length=200)),
                ('Relationship', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=200)),
                ('Donate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GuestEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=200)),
                ('hospital_address', models.CharField(max_length=400)),
                ('licno', models.CharField(max_length=200)),
                ('certificate', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('nameofgm', models.CharField(max_length=200)),
                ('departments', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_organ', models.PositiveSmallIntegerField(choices=[(0, 'HEART'), (1, 'LUNGS'), (2, 'KIDNEY'), (3, 'LIVER'), (4, 'TISSUE'), (5, 'PANCREAS'), (6, 'CORNEAS'), (7, 'EYES')], default=0, verbose_name='Organ')),
                ('bloodgroup', models.CharField(max_length=10, verbose_name='BGroup')),
                ('pub_date', models.DateTimeField(verbose_name='datetime')),
                ('expired', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrganReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
                ('district', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('bgroup', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=200)),
                ('organ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organ', to='app.Organ')),
            ],
        ),
        migrations.AddField(
            model_name='doctorrequestorgan',
            name='Hospitalname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospitalname', to='app.Hospital'),
        ),
        migrations.AddField(
            model_name='doctorrequestorgan',
            name='Organs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organs', to='app.Organ'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='app.Hospital'),
        ),
    ]
