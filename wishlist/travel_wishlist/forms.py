from django import forms
from .models import Place

'''
 Form to add in new data
'''
class NewPlaceForm(forms.ModelForm):
	class Meta:
		model = Place
		fields = ('name', 'visited')
