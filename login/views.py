from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def index(request):
    pass
    return render(request, 'mytest/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username'   , None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('mytest/index.html')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login.html', {"message": message})
    return render(request, 'login.html')


def logout(request):
    pass
    return redirect('mytest/index.html')
