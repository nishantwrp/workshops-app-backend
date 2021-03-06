# Generated by Django 2.2.10 on 2020-11-20 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_auto_20200303_2140'),
        ('workshop', '0020_auto_20200503_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('small_image_url', models.URLField(blank=True, null=True)),
                ('large_image_url', models.URLField(blank=True, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('joint_secy', models.ManyToManyField(blank=True, related_name='entity_joint_secy', to='authentication.UserProfile', verbose_name='Joint Secretary')),
                ('secy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entity_secy', to='authentication.UserProfile', verbose_name='Secretary')),
                ('subscribed_users', models.ManyToManyField(blank=True, related_name='entity_subscriptions', to='authentication.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('audience', models.CharField(blank=True, max_length=50)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('contacts', models.ManyToManyField(blank=True, related_name='organized_events', to='authentication.UserProfile')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='workshop.Entity')),
                ('interested_users', models.ManyToManyField(blank=True, related_name='interested_events', to='authentication.UserProfile')),
                ('tags', models.ManyToManyField(blank=True, related_name='tagged_events', to='workshop.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='EventResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('resource_type', models.CharField(choices=[('Prerequisite', 'Prerequisite'), ('Material', 'Material')], max_length=20)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='workshop.Event')),
            ],
        ),
    ]
