<<<<<<< HEAD
#coding:utf-8
from django.http import JsonResponse
from django.shortcuts import render_to_response,redirect,HttpResponse,render,HttpResponseRedirect
from .models import *
<<<<<<< HEAD
=======
from django.http import JsonResponse
>>>>>>> django项目2018/07/02 14:39:14 更新
import time,json,paramiko,ConfigParser,os
from datetime  import datetime
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.forms.models import model_to_dict
<<<<<<< HEAD
=======
from t_rms_host import *
>>>>>>> django项目2018/07/02 14:39:14 更新

# Create your views here.

def  index(request):
<<<<<<< HEAD
   
    return render(request, 'index.html', locals())

=======
    return render(request, 'index.html', locals())

def selectuser(request):
    name = str(request.POST['name']).strip()
    try:
        data = User.objects.filter(name__contains=name).values('id','idcard','name','mobile')
        if data:
            return JsonResponse(json.dumps({'data': list(data),'status':1}), safe=False)
        else:
            return JsonResponse(json.dumps({'data': '','status':0}), safe=False)
    except Exception as e:
        print e


def delteuser(request,id):
    return HttpResponse('删除的用户id为：{}'.format(id))

def updateuser(request,id):
    return HttpResponse('更新的用户id为：{}'.format(id))



def selecthouse(request):
    name = request.POST['name']
    try:
        house = SelectDB()
        data = house.selectHouse(name)
        if data:
            return JsonResponse(json.dumps({'data': list(data),'status': 1}), safe=False)
        else:
            return JsonResponse(json.dumps({'data': '','status':0}), safe=False)
    except Exception as e:
        print e



def deltehouse(request,id):
    return HttpResponse('删除的房源id为：{}'.format(id))

def updatehouse(request,id):
    return HttpResponse('更新的房源id为：{}'.format(id))

>>>>>>> django项目2018/07/02 14:39:14 更新

=======
#coding:utf-8
from django.http import JsonResponse
from django.shortcuts import render_to_response,redirect,HttpResponse,render,HttpResponseRedirect
from .models import *
from django.http import JsonResponse
import time,json,paramiko,ConfigParser,os
from datetime  import datetime
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.forms.models import model_to_dict
from t_rms_host import *
from  django.db.models import  Q
import qrcode
from addhouse import RentTest,Checkdata

# Create your views here.

def  index(request):
    return render(request, 'index.html', locals())

def  user(request):
    return render(request, 'user.html', locals())

def  house(request):
    return render(request, 'house.html', locals())

def  createcode(request):
    return render(request, 'code.html', locals())

def  additem(request):
    return render(request, 'additem.html', locals())


def selectuser(request):
    name = str(request.POST['name']).strip()
    pagecount = int(request.POST['pagecount'])
    page = int(request.POST['page'])
    order = int(request.POST['order'])
    print '每页显示:',pagecount,'条记录',',当前是第:',page,'页'

    try:
        count = User.objects.filter(Q(name__contains=name)|Q(mobile__contains=name)).values('id', 'idcard', 'name', 'mobile').count()
        if count :
             if order==1:
                 item="-id"#倒叙
             else:
                 item = "id"
             data = User.objects.filter(Q(name__contains=name)|Q(mobile__contains=name)).values('id', 'idcard', 'name', 'mobile').order_by(item)[(page - 1) * pagecount:page * pagecount]
             print count
             return JsonResponse(json.dumps({'data': list(data), 'status': 1, 'len': count}), safe=False)

        else:
            print 'no data check.....'
            return JsonResponse(json.dumps({'data': '', 'status': 0, 'len': 0}), safe=False)
    except Exception as e:
        print e
        return JsonResponse(json.dumps({'data': '', 'status': 0, 'len': 0}), safe=False)


def usercounts(request):
    name = str(request.POST['name']).strip()
    if name:
        count = User.objects.filter(Q(name__contains=name)|Q(mobile__contains=name)).values('id', 'idcard', 'name', 'mobile').count()
    else:
        count = User.objects.all().count()
    return JsonResponse(json.dumps({'count': count}), safe=False)




def delteuser(request,id):
    return HttpResponse('删除的用户id为：{}'.format(id))

def updateuser(request,id):
    return HttpResponse('更新的用户id为：{}'.format(id))



def selecthouse(request):
    name = request.POST['name']
    try:
        house = SelectDB()
        data = house.selectHouse(name)
        if data:
            return JsonResponse(json.dumps({'data': list(data),'status': 1,'len':len(data)}), safe=False)
        else:
            return JsonResponse(json.dumps({'data': '','status':0,'len':0}), safe=False)
    except Exception as e:
        print e



def deltehouse(request,id):
    return HttpResponse('删除的房源id为：{}'.format(id))

def updatehouse(request,id):
    return HttpResponse('更新的房源id为：{}'.format(id))


def fileload(request):
    if request.method == 'POST':
        try:
            name=datetime.now().strftime("%Y_%m_%d_%H%M%S")
            file_obj = request.FILES.get('file')
            print file_obj.name, file_obj.chunks()
            filename='{}-{}'.format(name,file_obj.name)
            for data in file_obj.chunks():
                print data,type(data)
                with open(filename,'w+') as  f:
                        f.write(data)
            return JsonResponse(json.dumps({'status':1}),safe=False)
        except Exception as e:
            print e
            return JsonResponse(json.dumps({'status':0}), safe=False)

def code(request):
    content = request.POST['content']
    import os
    path = os.path.abspath('static/images')
    filelist=os.listdir(path)
    if len(filelist)>0:
        for images in  filelist:
            if os.path.splitext(images)[-1]=='.png':
                os.remove(os.path.join(path,images))#删除原有的二维码照片

    if content:
        name = 'code_{}.png'.format(datetime.now().strftime("%Y_%m_%d_%H%M%S"))
        images = qrcode.make(content)
        with open('{}\{}'.format(path,name), 'wb') as f:
            images.save(f)

        codepath='static/images/{}'.format(name)
        print codepath
        return JsonResponse(json.dumps({'status': 1,'images':codepath}), safe=False)
    else:
        return JsonResponse(json.dumps({'status':0}),safe=False)

def addhouse(request):
    landermobile = request.POST['landermobile']
    rent_type = request.POST['rent_type']
    newestate = request.POST['newestate']
    housenum = int(request.POST['housenum'])
    type = request.POST['type']
    additems = RentTest(landermobile,rent_type,newestate,newestate)
    if type=='jz':
        try:
            additems.addhouse_jz(housenum)
        except Exception as e:
            print e
    else:
        for i in range(housenum):
            additems.addhouse_fs()
    return HttpResponse('{}/{}/{}/{}/{}'.format(landermobile,newestate,  housenum, rent_type, type))

def checkland(request):
    landcontent = request.POST['landcontent']
    if landcontent:
        checkdata = Checkdata()
        result = checkdata.selectlander(landcontent)
        print len(result)
        if  len(result)!=0:
            return JsonResponse(json.dumps({'result':result,'status':1,'len':len(result)}),safe=False)
        else:
            return JsonResponse(json.dumps({'result': "查询结果为空", 'status': 0,'len':0}), safe=False)
    else:
        return  JsonResponse(json.dumps({'result':"请输入查询条件",'status':0,'len':0}),safe=False)



>>>>>>> 自动化测试脚本2018/07/06 17:38:42 更新
