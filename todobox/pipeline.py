from tasks.models import Task, TaskBox
from login.models import TodoUser


def create_default_data(strategy, user, username, *args, **kwargs):
	try:
		u = user.todouser.if_registered
	except Exception, e:
		box = TaskBox.objects.create(user=user,title='Important things')
		Task.objects.create(box=box,title='Read the book')
		Task.objects.create(box=box,title='Call to mother')
		t = TodoUser(user = user)
		t.save()