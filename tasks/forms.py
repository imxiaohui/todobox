from django import forms

class AddItemForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Type your username',
		'class':'modal-input'}))