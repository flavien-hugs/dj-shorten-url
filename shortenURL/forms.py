# shortenURL/forms.py

from django import forms
from shortenURL.models import Shorten


class ShortenForm(forms.ModelForm):

	class Meta:
		model = Shorten
		fields = ['url']
