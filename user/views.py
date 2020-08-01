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

#
# def api_search(request):
#     data = [{'id': i.id, 'name': i.name, 'category': i.category.name, 'project': i.project.name,
#              'owner': i.owner.username, 'status': i.status.name, } for i in query]
#     res = {'code': 0, 'msg': '', 'cound': len(data), 'data': data}
#     return JsonResponse(res)

def demand_new(request):
    projects = Project.objects.all()
    status = Status.objects.all()
    users = User.objects.all()
    categorys=Category.objects.all()
    data = {'projects': projects, 'status': status, 'users': users,'categorys':categorys}
    return render(request, 'demand_new.html', data)


def api_demand_new(request):
    data = request.POST
    owner = data.get('owner')
    status = data.get('status')
    category = data.get('category')
    project = data.get('project')
    name = data.get('name')
    if owner not in ['', None] and status not in ['', None] and category not in ['', None] and name not in ['', None]:
        if len(name) <= 10:
            if not Requirement.objects.filter(name=name).exists():
                Requirement.objects.create(
                    name=name,
                    project_id=int(project),
                    category_id=int(category),
                    owner_id=int(owner),
                    status_id=int(status),
                    finish=0,
                )
                return JsonResponse({'code': 0})
            else:
                return JsonResponse({'code': 3, "msg": '需求名称已存在'})
        else:
            return JsonResponse({'code': 1, "msg": '名称超长'})

    else:
        return JsonResponse({'code': 2, "msg": '缺少必要参数'})


def demand_pool(request):
    projects = Project.objects.all()
    data = {'projects': projects}
    return render(request, 'demand_pool.html', data)


def api_demand_pool(request):
    return HttpResponse(123)


def api_demands(request):

    data=request.GET
    page=data.get('page')
    limit=data.get('limit')
    keyword=data.get('keyword')
    project=data.get('project')
    demands = Requirement.objects.filter(finish=0)
    if keyword:
        demands=demands.filter(name__contains=keyword)
    if project:
        demands=demands.filter(project_id=int(project))
    data = [{'id': i.id, 'name': i.name, 'category': i.category.name, 'project': i.project.name,
             'owner': i.owner.username, 'status': i.status.name, } for i in demands]
    if page and limit:
        page=int(page)
        limit=int(limit)

        data=data[(page-1)*limit:page*limit]
    res = {'code': 0, 'msg': '', 'count': len(demands), 'data': data}
    return JsonResponse(res)


def name_is_av(requset):
    name = requset.GET.get('name')
    if name not in [None, '']:
        if not Requirement.objects.filter(name=name).exists():
            return JsonResponse({'flag': True})
        else:
            return JsonResponse({'flag': False})
    else:
        return JsonResponse({'flag': None})


def error(request):
    msg = request.GET.get('msg')
    return render(request, 'error.html', {'msg': msg})


def api_delete(request):
    rid = request.POST.get('rid')
    if rid not in [None, '']:
        r = Requirement.objects.filter(id=int(rid))
        if r:
            r.delete()
            return JsonResponse({'code': 0})
        else:
            return JsonResponse({'code': 1, 'msg': '需求不存在'})
    else:
        return JsonResponse({'code': 2, 'msg': '缺少id'})


def api_archive(request):
    rid = request.POST.get('rid')
    if rid not in [None, '']:
        r = Requirement.objects.filter(id=int(rid))
        if r:
            r.update(finish=1)
            return JsonResponse({'code': 0})
        else:
            return JsonResponse({'code': 1, 'msg': '需求不存在'})
    else:
        return JsonResponse({'code': 2, 'msg': '缺少id'})

def demand_update(request):
    rid = request.GET.get('rid')
    if rid:
        r = Requirement.objects.filter(id=int(rid))
        if r.exists():
            r=r.first()
            projects=Project.objects.all()
            status = Status.objects.all()
            users = User.objects.all()
            categorys=Category.objects.all()
            return render(request,'demand_update.html',{"requirement":r,'projects':projects,'status':status,'users':users,'categorys':categorys})
        else:
            return JsonResponse({'code': 1, 'msg': '需求不存在'})
    else:
        return JsonResponse({'code': 2, 'msg': '缺少id'})


def api_update(request):
    data = request.POST
    owner = data.get('owner')
    status = data.get('status')
    category = data.get('category')
    project = data.get('project')
    name = data.get('name')
    rid=data.get('rid')
    if owner not in ['', None] and status not in ['', None] and category not in ['', None] and name not in ['', None]:
        if len(name) <= 10:
            if not Requirement.objects.filter(name=name).exists() or Requirement.objects.filter(id=int(rid)).first().name == name:
                Requirement.objects.filter(id=int(rid)).update(
                    name=name,
                    project_id=int(project),
                    category_id=int(category),
                    owner_id=int(owner),
                    status_id=int(status),
                    finish=0,
                )
                return JsonResponse({'code': 0})
            else:
                return JsonResponse({'code': 3, "msg": '需求名称已存在'})
        else:
            return JsonResponse({'code': 1, "msg": '名称超长'})

    else:
        return JsonResponse({'code': 2, "msg": '缺少必要参数'})


