# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('categorie', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('salutation', models.CharField(default='', max_length=10)),
                ('nom', models.CharField(default='', max_length=100)),
                ('prenom', models.CharField(default='', max_length=100)),
                ('titre', models.CharField(default='', max_length=100)),
                ('telephone', models.CharField(default='', max_length=20)),
                ('autre_telephone', models.CharField(default='', max_length=20)),
                ('courriel', models.CharField(default='', max_length=50)),
                ('autre_courriel', models.CharField(default='', max_length=50)),
                ('organisation', models.CharField(blank=True, default='', max_length=100)),
                ('date_entree', models.DateField(verbose_name="Date d'inscription", default='2008-01-01')),
                ('adresse1', models.CharField(default='', max_length=50)),
                ('adresse2', models.CharField(blank=True, default='', max_length=50)),
                ('ville', models.CharField(default='', max_length=50)),
                ('province', models.CharField(default='', max_length=10)),
                ('code_postal', models.CharField(default='', max_length=7)),
                ('carte_noel', models.BooleanField(default=False)),
                ('categorie', models.ForeignKey(to='crm.Categorie', default='')),
            ],
        ),
        migrations.CreateModel(
            name='Dons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('annee', models.IntegerField()),
                ('don', models.IntegerField(default=0)),
                ('contact', models.ForeignKey(to='crm.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('texte', models.CharField(default='', max_length=2000)),
                ('utilisateur', models.CharField(default='', max_length=50)),
                ('contact', models.ForeignKey(to='crm.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nom', models.CharField(default='', max_length=100)),
                ('date_entree', models.DateTimeField(verbose_name='Date entree', blank=True, default='')),
                ('telephone', models.CharField(default='', max_length=20)),
                ('adresse1', models.CharField(default='', max_length=50)),
                ('adresse2', models.CharField(blank=True, default='', max_length=50)),
                ('ville', models.CharField(default='', max_length=50)),
                ('province', models.CharField(default='', max_length=10)),
                ('code_postal', models.CharField(default='', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='StatutCampagne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('statut', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StatutContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('statut', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='dons',
            name='type',
            field=models.ForeignKey(to='crm.Type', default=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='statut_campagne',
            field=models.ForeignKey(to='crm.StatutCampagne'),
        ),
        migrations.AddField(
            model_name='contact',
            name='statut_contact',
            field=models.ForeignKey(to='crm.StatutContact'),
        ),
    ]
