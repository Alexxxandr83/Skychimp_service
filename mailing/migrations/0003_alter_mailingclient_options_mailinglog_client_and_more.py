# Generated by Django 4.2.4 on 2023-08-19 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_mailingclient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingclient',
            options={'verbose_name': 'Список рассылки', 'verbose_name_plural': 'Списки рассылок'},
        ),
        migrations.AddField(
            model_name='mailinglog',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='mailingclient',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.client', verbose_name='клиент'),
        ),
        migrations.AlterField(
            model_name='mailingclient',
            name='mailing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings', verbose_name='рассылка'),
        ),
        migrations.AlterField(
            model_name='mailinglog',
            name='mailing_service_response',
            field=models.TextField(blank=True, null=True, verbose_name='Ответ почтового сервера, если он был'),
        ),
    ]