from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from forms import LoginForm

def loginpage(request):
	loginform = LoginForm()
	return render(request, 'login/login-index.html',{
			'loginform':loginform
		})

@require_http_methods(["POST"])
def login(request):
	pass


@require_http_methods(["POST"])
def register():
	pass
