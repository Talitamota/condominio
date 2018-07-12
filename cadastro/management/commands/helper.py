import csv

from cadastro.models import Apartamento, Bloco

class LinhaValue:

	def __init__(self,apartamento):
		self.apartamento = apartamento

	@property
	def numero(self):
		return self.apartamento['Unidade']

	@property
	def bloco(self):
		return self.apartamento['Bloco']


class Planilha:

    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.data = []

    def load(self):
        with open(self.nome_arquivo) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')

            for row in reader:
                linha = LinhaValue(row)
                self.data.append(linha)

        print(self.data[0])

    def list(self):
        return self.data

def criar_apartamento(bloco, linha):
    
    return Apartamento.objects.create(
        numero=linha.numero,
        bloco=bloco)






	
	