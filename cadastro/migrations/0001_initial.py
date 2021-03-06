# Generated by Django 2.0.6 on 2018-06-25 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Apartamento',
                'verbose_name_plural': 'Apartamentos',
            },
        ),
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('Prainha', 'Prainha'), ('Grumari', 'Grumari')], max_length=30)),
                ('numero', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=1)),
            ],
            options={
                'verbose_name': 'Bloco',
                'verbose_name_plural': 'Blocos',
            },
        ),
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('telefone1', models.CharField(blank=True, max_length=30, null=True, verbose_name='Telefone residencial')),
                ('telefone2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Telefone celular')),
                ('numero_cpf', models.CharField(blank=True, max_length=50, null=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=50, null=True, verbose_name='RG')),
                ('orgao_expeditor', models.CharField(blank=True, max_length=50, null=True, verbose_name='Orgão expeditor')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('sexo', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='', max_length=50, null=True)),
                ('numero_apartamento', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cadastro.Apartamento', verbose_name='Número do Apartamento')),
            ],
            options={
                'verbose_name': 'Morador',
                'verbose_name_plural': 'Moradores',
            },
        ),
        migrations.AddField(
            model_name='apartamento',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Bloco'),
        ),
    ]
