# Generated by Django 2.0 on 2018-10-23 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DonationRequest', '0002_auto_20181019_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationreq',
            old_name='Doante',
            new_name='Donate',
        ),
        migrations.RemoveField(
            model_name='donationreq',
            name='Spec_item1',
        ),
        migrations.RemoveField(
            model_name='donationreq',
            name='Spec_item2',
        ),
        migrations.RemoveField(
            model_name='donationreq',
            name='Spec_item3',
        ),
    ]
