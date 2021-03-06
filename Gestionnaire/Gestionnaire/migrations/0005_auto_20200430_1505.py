# Generated by Django 2.1.7 on 2020-04-30 14:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gestionnaire', '0004_auto_20200430_1201'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='archiveassignation',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='archiveassignation',
            name='support',
        ),
        migrations.RemoveField(
            model_name='archiveassignation',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='ArchiveProduit',
        ),
        migrations.AlterUniqueTogether(
            name='archiveticket',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='archiveticket',
            name='initiateur',
        ),
        migrations.RemoveField(
            model_name='archiveticket',
            name='produit',
        ),
        migrations.AlterModelOptions(
            name='assignation',
            options={'ordering': ['-dateAssignation']},
        ),
        migrations.AlterModelOptions(
            name='categorie',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='categorie',
            name='id',
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Nom'),
        ),
        migrations.AlterUniqueTogether(
            name='assignation',
            unique_together={('categorie', 'ticket', 'support')},
        ),
        migrations.DeleteModel(
            name='ArchiveAssignation',
        ),
        migrations.DeleteModel(
            name='ArchiveTicket',
        ),
    ]
