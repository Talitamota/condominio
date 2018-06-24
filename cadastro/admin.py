from django.contrib import admin

from .models import Bloco


class BlocoAdmin(admin.ModelAdmin):	
	list_display = ('nome','numero')


admin.site.register(Bloco, BlocoAdmin)
