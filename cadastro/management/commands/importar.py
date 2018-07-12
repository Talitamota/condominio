

from django.core.management.base import BaseCommand

from cadastro.models import Bloco
from .helper import Planilha, criar_apartamento


class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument(
            '--bloco-id',
            action='store',
            dest='bloco_id',
        )

        parser.add_argument(
            '--nome-arquivo',
            action='store',
            dest='nome_arquivo',
        )

    def handle(self, *args, **options):

        nome_arquivo = options.get('nome_arquivo')
        bloco_id = options.get('bloco_id')
        bloco = Bloco.objects.get(pk=bloco_id)

        planilha =  Planilha(f"arquivos/{nome_arquivo}")
        planilha.load()

        for linha in planilha.list():

            apartamento = criar_apartamento(bloco, linha)

            print(f"{apartamento}")

