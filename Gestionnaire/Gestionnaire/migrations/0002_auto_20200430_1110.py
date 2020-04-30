# Generated by Django 2.1.7 on 2020-04-30 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gestionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignation',
            name='categorie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Gestionnaire.Categorie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='archiveproduit',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='archiveproduit',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='archiveproduit',
            name='version',
            field=models.CharField(max_length=10, verbose_name='Version'),
        ),
        migrations.AlterField(
            model_name='archiveticket',
            name='titre',
            field=models.CharField(max_length=100, verbose_name='Objet du ticket'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='version',
            field=models.CharField(max_length=10, verbose_name='Version'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='titre',
            field=models.CharField(max_length=100, verbose_name='Objet du ticket'),
        ),
        migrations.AlterUniqueTogether(
            name='assignation',
            unique_together={('categorie', 'ticket', 'support', 'gravite', 'etat', 'delai', 'dateAssignation')},
        ),
        migrations.AlterUniqueTogether(
            name='categorie',
            unique_together={('name', 'data', 'description')},
        ),
    ]