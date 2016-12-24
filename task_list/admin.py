
from django.contrib import admin
from task_list.models import  Todolist, Category
# Register your models here.




class TodolistAdmin(admin.ModelAdmin):
    fields = ['todolist_list','todolist_description', 'todolist_category', 'todolist_date_published', 'todolist_date_finished', 'todolist_priority', 'todolist_done', 'todolist_user']
    search_fields = ['todolist_category']
    list_filter = ['todolist_date_finished']



"""class ListInline(admin.TabularInline):
    model = Todolist"""


admin.site.register(Todolist, TodolistAdmin)
admin.site.register(Category)