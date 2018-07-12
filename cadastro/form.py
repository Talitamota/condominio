from django import forms

from cadastro.models import Apartamento

class ApartamentoForm(forms.ModelForm):

	class Meta:
		model = Apartamento
		fields = "__all__"


