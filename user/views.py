from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.contrib import auth
import xlrd
from xlrd import xldate_as_datetime
from user.models import *
from django.db import connection
from user.models import *

# Create your views here.

def init_db(request):
    return HttpResponse(123)


#     Author.objects.all().delete()
#     AuthorDetail.objects.all().delete()
#     Publisher.objects.all().delete()
#     Book.objects.all().delete()
#     cursor = connection.cursor()
#     sql1 = "UPDATE sqlite_sequence SET seq =0 WHERE name='user_author';"
#     sql2 = "UPDATE sqlite_sequence SET seq =0 WHERE name='user_authordetail';"
#     sql3 = "UPDATE sqlite_sequence SET seq =0 WHERE name='user_publisher';"
#     sql4 = "UPDATE sqlite_sequence SET seq =0 WHERE name='user_book';"
#     sql5 = "UPDATE sqlite_sequence SET seq =0 WHERE name='user_book_author';"
#
#     cursor.execute(sql5)
#     cursor.execute(sql1)
#     cursor.execute(sql2)
#     cursor.execute(sql3)
#     cursor.execute(sql4)
#     cursor.close()


def index(requset):
    return render(requset, 'index.html')


def login(request):
    return HttpResponse(123)


def api_login(request):
    return HttpResponse(123)


def logout(request):
    return HttpResponse(123)


def api_logout(request):
    return HttpResponse(123)


def search(request):
    return HttpResponse(123)


def api_search(request):
    return HttpResponse(123)


def demand_new(request):
    return render(request, 'demand_new.html')


def api_new(request):
    return HttpResponse(123)


def demand_pool(request):
    return render(request, 'demand_pool.html')


def api_demand_pool(request):
    return HttpResponse(123)
def api_demands(request):
    demands=Requirement.objects.all()    # for i in data
    data=[{'id':i.id,'name':i.name,'category':i.category,'project':Project.objects.get(id=i.project_id).name,'owner':i.owner,'status':i.status_id,'finish':i.finish} for i in demands]

    res={'code':0,'msg':'','cound':len(data),'data':data}
    return JsonResponse(res)

