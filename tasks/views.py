from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from tasks.models import TaskBox, Task
from django.shortcuts import render
from tasks.forms import AddItemForm
from django.http import HttpResponse, HttpResponseRedirect

@login_required(login_url='/')
def boxes(request):
	boxes = TaskBox.objects.filter(user=request.user)
	additemform = AddItemForm()
	col1 = boxes[0::3]
	col2 = boxes[1::3]
	col3 = boxes[2::3]
	return render(request,'tasks/tasks-index.html',{
		'col1':col1,
		'col2':col2,
		'col3':col3,
		'additemform':additemform
		})

@login_required(login_url='/')
@require_http_methods(["POST"])
def add_box(request):
	form = AddItemForm(request.POST)
	if form.is_valid():
		title = form.cleaned_data['title']
		t = TaskBox(user = request.user,title=title)
		t.save()
		return HttpResponseRedirect('/')
	return HttpResponse('invalid form')

@login_required(login_url='/')
@require_http_methods(["POST"])
def add_task(request):
	form = AddItemForm(request.POST)
	if form.is_valid():
		title = form.cleaned_data['title']
		box_pk= request.POST.get('box_id','')
		box =TaskBox.objects.get(pk=box_pk)
		t = Task(box = box,title=title)
		t.save()
		return HttpResponseRedirect('/')
	return HttpResponse('invalid form')

@login_required(login_url='/')
@require_http_methods(["POST"])
def done_task(request):
	task_id = request.POST.get('task_id','')
	
	Task.objects.get(pk = int(task_id)).delete()
	return HttpResponseRedirect('/')

@login_required(login_url='/')
@require_http_methods(["POST"])
def delete_box(request):
	box_id = request.POST.get('delete_box_id','')
	TaskBox.objects.get(pk = int(box_id)).delete()
	return HttpResponseRedirect('/')


