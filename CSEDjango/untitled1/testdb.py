# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from TestModel.models import Test


# 数据库操作

def test_database(request):
    test1 = Test(name='cse')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def show_table(request):
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


def search_member(request):
    context = {}
    if request.POST:
        context['remind'] = '你搜索的目标是：'
        context['rlt'] = request.POST['q']
        Test.objects.exists()
        if Test.objects.exists(name='q'):
            context['result'] = '用户存在， id为：' + repr(Test.objects.get(name='q').id)
        else:
            context['result'] = '用户不存在'
    return render(request, 'search_db.html', context)






