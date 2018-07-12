from django.contrib import admin

from cadastro.models import Bloco, Apartamento, Morador
from cadastro.form import ApartamentoForm


class BlocoAdmin(admin.ModelAdmin):	
	list_display = ('nome','numero')


class ApartamentoAdmin(admin.ModelAdmin):
	form = ApartamentoForm
	list_display = ('numero', 'bloco')
	list_display_links = ('numero',)
	list_per_page = 10
	search_fields = ['=numero']
	list_filter = ('bloco',)
	radio_fields = {"bloco": admin.HORIZONTAL}
	show_full_result_count = False


class MoradorAdmin(admin.ModelAdmin):
	list_display = ('nome_completo','numero_apartamento')



admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Apartamento, ApartamentoAdmin)	
admin.site.register(Morador, MoradorAdmin)
