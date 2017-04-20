from django.shortcuts import render, redirect
# -*- coding:utf8-*-
# Create your views here.
from django.shortcuts import HttpResponse
from cmdb import models as cmdb_models
from scripts import functions


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        user = cmdb_models.UserInfo.objects.filter(username=user, password=pwd)
        print(user)
        if user:
            return redirect("/dbms/index")
        else:
            return redirect("http://www.bing.com")
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        email = request.POST.get('Email', None)
        user_info = cmdb_models.UserInfo.objects.filter(username=user)
        if user_info:
            # username and password is existe
            #
            pass
        else:
            cmdb_models.UserInfo.objects.create(username=user, password=pwd, emails=email)
            return redirect('/dbms/login')
    else:
        return render(request, 'register.html')


def inception(request):
    review_users = ['think', 'zhangsan', '2343', '23423', '23423423']
    if request.method == 'POST':
        host_ip = request.POST.get('dbhost', None)
        db_name = request.POST.get('dbname', None)
        db_port = request.POST.get('dbport', 3306)
        review_user = request.POST.get('select_user', None)
        sql_content = 'use ' + db_name + '; ' + request.POST.get('sql_area', None)
        w_id = functions.get_uuid()
        work_user = 'think'
        db_ip = functions.num2ip('num', host_ip)
        cmdb_models.InceptionWorkOrderInfo.objects.create(
            work_order_id=w_id,
            work_user=work_user,
            review_user=review_user,
            db_host=db_ip,
            db_name=db_name
        )
        cmdb_models.InceptionWorkSQL.objects.create(
            sql_content=sql_content,
            work_order_id=w_id
        )

        result = functions.ince_run_sql(host_ip, sql_content, port=db_port)
        return render(request, 'inception.html', {'ince_result': result[1:], 'review_users': review_users})
    else:
        return render(request, 'inception.html', {'review_users': review_users})


def backup(request):
    return HttpResponse('backup')


def install(request):
    return HttpResponse('install')
