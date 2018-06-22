from django.shortcuts import render
from django.contrib import auth
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import hashlib
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login_action(request):
   if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # 登录
            request.session['user'] = username # 将 session 信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html', {'error': '用户名或密码错误'})



def event_manage(request):
    username = request.session.get('user', '')
    if len(username) != 0:
        return render(request, "event_manager.html", {"user":username})
    else:
        return render(request,'index.html')

def page_not_found(request):
    return render_to_response('404.html')
#
#
def page_error(request):
    return render_to_response('500.html')