# Generated by Django 2.2.10 on 2020-11-20 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0021_entity_event_eventresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club_events', to='workshop.Club'),
        ),
        migrations.AddField(
            model_name='tag',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entity_tags', to='workshop.Entity'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entity_workshops', to='workshop.Entity'),
        ),
        migrations.AddField(
            model_name='workshopresource',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_resources', to='workshop.Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entity_events', to='workshop.Entity'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='workshop.Club'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workshops', to='workshop.Club'),
        ),
        migrations.AlterField(
            model_name='workshopresource',
            name='workshop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='workshop.Workshop'),
        ),
        migrations.DeleteModel(
            name='EventResource',
        ),
    ]
