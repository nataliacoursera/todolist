from django.forms import ModelForm, forms
from models import Todolist, User, Category
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.forms import User
import datetime


class TodolistForm(ModelForm):


    #current_user=forms.Charfielnd(auth.get_user(request=username), label = 'username')
    class Meta:

        model = Todolist


        exclude = ['todolist_done', 'todolist_user']
        #field =    [{'todolist_date_published': datetime.datetime.now()}]
    def save(self, user, time_now):
        obj=super(TodolistForm, self).save(commit=False)
        obj.todolist_user=user
        obj.todolist_date_published=time_now
        return obj.save()

class CategoryForm(ModelForm):
    class Meta:
        model=Category

    fields=['group_todolist']
