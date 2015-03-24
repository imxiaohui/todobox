from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todobox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'login.views.loginpage'),
    url(r'^register/$', 'login.views.register', name='register'),
    url(r'^logout/$', 'login.views.logout_view', name='logout'),
    url(r'^login/$', 'login.views.login_view', name='login'),

    url(r'^taskbox/$', 'tasks.views.boxes', name='boxes'),

    url(r'^addbox/$', 'tasks.views.add_box', name='addbox'),
    url(r'^addtask/$', 'tasks.views.add_task', name='addtask'),
    url(r'^donetask/$', 'tasks.views.done_task', name='donetask'),
    url(r'^deletebox/$', 'tasks.views.delete_box', name='deletebox'),
)
