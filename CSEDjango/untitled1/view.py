from django.http import HttpResponse


def hello(request):
    return HttpResponse("<html><body><h1>春晓</h1><p>春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。</p><p>注意，浏览器忽略了源代码中的排版（省略了多余的空格和换行）。</p></body></html>")