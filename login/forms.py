from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Type your username',
		'class':'modal-login-input'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type your password',
		'class':'modal-login-input'}))

class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Type your username',
		'class':'modal-login-input'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type your password',
		'class':'modal-login-input'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Type your email',
		'class':'modal-login-input'}))
	fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Type your full name',
		'class':'modal-login-input'}))