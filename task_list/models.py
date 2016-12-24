
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.dateparse import datetime, parse_datetime

from django.template import RequestContext
# Create your models here.

class Category(models.Model):
    group_todolist = models.CharField(max_length =20)

    def __unicode__(self):
        return self.group_todolist


class Todolist(models.Model):
    class Meta():
        db_table = "TO_DO_LIST"
    todolist_list = models.CharField(max_length = 100)
    todolist_date_published = models.DateTimeField(auto_now_add=True)
    todolist_date_finished = models.CharField(max_length =20)
    todolist_category = models.ForeignKey(Category)
    todolist_priority = models.IntegerField(default=0)
    todolist_done = models.BooleanField(default=False)
    todolist_description = models.CharField(max_length = 500)
    todolist_user = models.ForeignKey(User)


    def __unicode__(self):
        return self.todolist_list