from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^todolist/get/(?P<TO_DO_LIST_id>\d+)/$', 'task_list.views.todo'),
    url(r'^$', 'task_list.views.todolist'),
    url(r'^todolist/add_category/$', 'task_list.views.new_category'),
    url(r'^todolist/addnew/$', 'task_list.views.addnew'),
    url(r'^todolist/addnew/savetodolist/$', 'task_list.views.savetodolist'),
    url(r'^page/(\d+)/todolist/done/(?P<TO_DO_LIST_id>\d+)/$', 'task_list.views.done'),
    url(r'^todolist/done/(?P<TO_DO_LIST_id>\d+)/$', 'task_list.views.done'),
    url(r'^page/(\d+)/todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/$', 'task_list.views.delete_confirm'),
    url(r'^page/(\d+)/todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/delete/$', 'task_list.views.delete'),
    url(r'^todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/$', 'task_list.views.delete_confirm'),
    url(r'^todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/delete/$', 'task_list.views.delete'),
    url(r'^page/(\d+)/$', 'task_list.views.todolist'),

    url(r'^todolist/add_category/save_category/$', 'task_list.views.save_category'),

)