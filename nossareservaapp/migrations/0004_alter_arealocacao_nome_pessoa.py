# Generated by Django 3.2 on 2022-06-22 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nossareservaapp', '0003_auto_20220622_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arealocacao',
            name='nome_pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locacoes', to='nossareservaapp.usuario'),
        ),
    ]