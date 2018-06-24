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
	pass


class Apartamento(models.Model):

	numero = models.CharField(max_length=4)

	bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)

	moradores = models.ManyToManyField(Morador)


