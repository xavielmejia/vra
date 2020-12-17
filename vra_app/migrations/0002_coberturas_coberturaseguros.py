# Generated by Django 3.1.4 on 2020-12-03 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vra_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coberturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='CoberturaSeguros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=255)),
                ('cobertura_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vra_app.coberturas')),
                ('seguro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vra_app.seguros')),
            ],
        ),
    ]
