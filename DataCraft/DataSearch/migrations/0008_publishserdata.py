# Generated by Django 2.0.2 on 2018-03-01 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataSearch', '0007_auto_20180227_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
                ('data_classification', models.CharField(choices=[('Public', 'Public'), ('Sensitive', 'Sensitive'), ('Protected', 'Protected')], max_length=200, verbose_name='data_classification')),
                ('category', models.CharField(blank=True, choices=[('City Infrastructure', 'City Infrastructure'), ('City Management and Ethics', 'City Management and Ethics'), ('Culture and Recreation', 'Culture and Recreation'), ('Economy and Community', 'Economy and Community'), ('Energy and Environment', 'Energy and Environment'), ('Geographic Locations and Boundaries', 'Geographic Locations and Boundaries'), ('Health and Social Services', 'Health and Social Services'), ('Housing and Buildings', 'Housing and Buildings'), ('Public Safety', 'Public Safety'), ('Transportation', 'Transportation')], max_length=200, null=True, verbose_name='category_type')),
                ('data_change_frequency', models.CharField(choices=[('Not updated (historical only)', 'Not updated (historical only)'), ('As needed', 'As needed'), ('Annually', 'Annually'), ('Bi-annually', 'Bi-annually'), ('Quarterly', 'Quarterly'), ('Bi-monthly', 'Bi-monthly'), ('Monthly', 'Monthly'), ('Bi-weekly', 'Bi-weekly'), ('Weekly', 'Weekly'), ('Daily', 'Daily'), ('Hourly', 'Hourly'), ('Multiple times hourly', 'Multiple times hourly'), ('Streaming', 'Streaming')], max_length=200, verbose_name='data_change_frequency ')),
                ('automated_fashion', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unsure', 'Unsure')], max_length=200, verbose_name='Automated_Fashion')),
                ('dataset_come_from', models.CharField(choices=[('API connect', 'API connect'), ('Hadoop', 'Hadoop'), ('EDW', 'EDW'), ('Reltio', 'Reltio'), ('EODS', 'EODS')], max_length=200, verbose_name='Sataset_Come_From')),
                ('automation_option', models.BooleanField(default=False)),
                ('upload', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('data_classification_comments', models.CharField(max_length=500, verbose_name='classification_comment')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataSearch.Client', verbose_name='publisher')),
            ],
        ),
    ]
