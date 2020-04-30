# Generated by Django 2.1.7 on 2020-04-30 10:30

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionnaire', '0002_auto_20200430_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='data',
            new_name='supports',
        ),
        migrations.AddField(
            model_name='categorie',
            name='tickets',
            field=picklefield.fields.PickledObjectField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='categorie',
            unique_together={('name', 'tickets', 'supports', 'description')},
        ),
    ]
