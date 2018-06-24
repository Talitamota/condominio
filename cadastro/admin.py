from django.contrib import admin

from .models import Bloco, Apartamento, Morador


class BlocoAdmin(admin.ModelAdmin):	
	list_display = ('nome','numero')


admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Apartamento)
admin.site.register(Morador)
