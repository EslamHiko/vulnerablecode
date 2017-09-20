# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImpactedPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(blank=True, help_text='Package platform eg:maven', max_length=50)),
                ('name', models.CharField(blank=True, help_text='Package name', max_length=50)),
                ('version', models.CharField(blank=True, help_text='Package version', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PackageReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repository', models.CharField(blank=True, help_text='Repository URL eg:http://central.maven.org', max_length=50)),
                ('platform', models.CharField(blank=True, help_text='Platform eg:maven', max_length=50)),
                ('name', models.CharField(blank=True, help_text='Package reference name eg:org.apache.commons.io', max_length=50)),
                ('version', models.CharField(blank=True, help_text='Reference version', max_length=50)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.Package')),
            ],
        ),
        migrations.CreateModel(
            name='ResolvedPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.Package')),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(blank=True, help_text='Summary of the vulnerability', max_length=50)),
                ('cvss', models.FloatField(help_text='CVSS Score', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VulnerabilityReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, help_text='Source(s) name eg:NVD', max_length=50)),
                ('reference_id', models.CharField(blank=True, help_text='Reference ID, eg:CVE-ID', max_length=50)),
                ('url', models.URLField(blank=True, help_text='URL of Vulnerability data', max_length=1024)),
                ('vulnerability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.Vulnerability')),
            ],
        ),
        migrations.AddField(
            model_name='resolvedpackage',
            name='vulnerability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.Vulnerability'),
        ),
        migrations.AddField(
            model_name='impactedpackage',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.Package'),
        ),
        migrations.AddField(
            model_name='impactedpackage',
            name='vulnerability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.Vulnerability'),
        ),
        migrations.AlterUniqueTogether(
            name='vulnerabilityreference',
            unique_together=set([('vulnerability', 'source', 'reference_id', 'url')]),
        ),
        migrations.AlterUniqueTogether(
            name='impactedpackage',
            unique_together=set([('vulnerability', 'package')]),
        ),
    ]