# Generated by Django 2.2.6 on 2019-10-10 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20191009_1206'),
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='council',
            name='joint_secy1',
        ),
        migrations.RemoveField(
            model_name='council',
            name='joint_secy2',
        ),
        migrations.AddField(
            model_name='council',
            name='joint_secy',
            field=models.ManyToManyField(related_name='councils_joint_secy', to='authentication.UserProfile'),
        ),
        migrations.AlterField(
            model_name='council',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='council',
            name='secy',
        ),
        migrations.AddField(
            model_name='council',
            name='secy',
            field=models.ManyToManyField(related_name='councils_secy', to='authentication.UserProfile'),
        ),
    ]