from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from tasks.models import TaskBox, Task

def loginpage(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/taskbox')
	loginform = LoginForm()
	registerform = RegisterForm()
	return render(request, 'login/login-index.html',{
			'loginform':loginform,
			'registerform':registerform
		})

@require_http_methods(["POST"])
def login_view(request):
	form = LoginForm(request.POST)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']

		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/taskbox')
		return HttpResponse('valid form')
	return HttpResponse('invalid form')


@require_http_methods(["POST"])
def register(request):
	form = RegisterForm(request.POST)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		email = form.cleaned_data['email']
		fullname = form.cleaned_data['fullname']

		u = User.objects.create_user(username,email,password,first_name=fullname)
		box = TaskBox.objects.create(user=u,title='Important things')
		Task.objects.create(box=box,title='Read the book')
		Task.objects.create(box=box,title='Call to mother')
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)

		return HttpResponseRedirect('/taskbox')
	else:
		return HttpResponse('bad')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
