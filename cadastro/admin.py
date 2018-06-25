from django.contrib import admin

from .models import Bloco, Apartamento, Morador


class BlocoAdmin(admin.ModelAdmin):	
	list_display = ('nome','numero')


class ApartamentoAdmin(admin.ModelAdmin):
	list_display = ('numero', 'bloco')


class MoradorAdmin(admin.ModelAdmin):
	list_display = ('nome_completo','numero_apartamento')


admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Apartamento, ApartamentoAdmin)	
admin.site.register(Morador, MoradorAdmin)
