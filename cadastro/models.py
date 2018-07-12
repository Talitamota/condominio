# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Bloco(models.Model):

	nome =  models.CharField(max_length=30,
			choices=(('Prainha','Prainha'), ('Grumari', 'Grumari')))

	numero = models.CharField(max_length=1,
			choices=(('1','1'),('2','2')))

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Bloco'
		verbose_name_plural = 'Blocos'


class Morador(models.Model):

	numero_apartamento = models.ForeignKey('Apartamento',
			verbose_name=u'Número do Apartamento',on_delete=models.CASCADE)

	nome = models.CharField(max_length=50)

	sobrenome = models.CharField(max_length=50)

	email = models.CharField(max_length=50,
			null=True, blank=True)

	telefone1 = models.CharField('Telefone residencial',	
			max_length=30, null=True, blank=True)

	telefone2 = models.CharField('Telefone celular',
			max_length=30, null=True, blank=True)
	
	numero_cpf = models.CharField('CPF',
			max_length=50, null=True, blank=True)
	
	rg = models.CharField('RG',
			max_length=50, null=True, blank=True)

	orgao_expeditor = models.CharField(u'Orgão expeditor',
			max_length=50, null=True, blank=True)
	
	data_nascimento = models.DateField('Data de nascimento',
			null=True, blank=True)
	
	sexo = models.CharField(max_length=50,
			null=True, blank=True, default='', choices=(
				('Masculino', 'Masculino'),
				('Feminino', 'Feminino')))

	def nome_completo(self):
		return '%s %s' %(self.nome, self.sobrenome)


	def __str__(self):
		return self.nome_completo()

	class Meta:
		verbose_name = 'Morador'
		verbose_name_plural = 'Moradores'


class Apartamento(models.Model):

	numero = models.CharField(max_length=4)

	bloco = models.ForeignKey(Bloco,
			on_delete=models.CASCADE)

	def __str__(self):
		return self.numero

	class Meta:
		verbose_name = 'Apartamento'
		verbose_name_plural = 'Apartamentos'
		ordering = ['numero']


