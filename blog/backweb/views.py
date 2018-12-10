from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from backweb.models import User
from backweb.models import Article, ArticleType
from django.urls import reverse
# Create your views here.


def register(request):
    """定义注册"""
    if request.method == 'GET':
        return render(request, 'backweb/register.html')

    if request.method == 'POST':
        # 1.取到用户名密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # 2.判断用户是否被注册
        user = User.objects.filter(username=username).first()

        if user:
            # 存在账号时
            errors = '该账号已经被注册，请更换账号'
            return render(request, 'backweb/register.html', {'errors': errors})

        # 3.判断两次密码输入是否相同
        if password and password2:
            if password != password2:
                errors = '两次密码不相等，重新注册'
                return render(request, 'backweb/register.html', {'errors': errors})
        else:
            errors = '密码不能为空，重新注册'
            return render(request, 'backweb/register.html', {'errors': errors})

        # 4.实现注册，数据库录入数据
        User.objects.create(username=username, password=password)
        # 跳转登录页面
        return HttpResponseRedirect('/backweb/login/')


def login(request):
    """定义登录界面"""
    if request.method == 'GET':
        return render(request, 'backweb/login.html')

    if request.method == 'POST':
        # 1.取得账号密码
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 2.判断账号是否存在
        user = User.objects.filter(username=username).first()
        if user:
            if user.password != password:
                err_pw = '账号密码不匹配，重新登录'
                return render(request, 'backweb/login.html', {'err_pw': err_pw})
        else:
            err_user = '账号不存在'
            return render(request, 'backweb/login.html', {'err_user': err_user})

        # 3.使用session实现登录保持操作，设置session_id值，value为随机字符串
        # 并在django_session表中存入session
        request.session['user_id'] = user.id

        # 4.跳转首页
        res = HttpResponseRedirect('/backweb/index/')
        return res


def logout(request):
    if request.method == 'GET':
        del request.session['user_id']
        return HttpResponseRedirect(reverse('backweb:login'))


def index(request):
    """定义管理主页"""
    if request.method == 'GET':
        article = Article.objects.all().count()
        return render(request, 'backweb/index.html', {'article': article})


def article(request):
    """定义文章页面"""
    if request.method == 'GET':
        from django.core.paginator import Paginator
        # 获取所有文章
        article = Article.objects.all()
        # 获取当前网页page,没有page参数就为1
        page = int(request.GET.get('page', 1))
        # 将所有文章分为五个一页分块
        paginator = Paginator(article, 5)
        # 获取当前文章分块对象
        page = paginator.page(page)
        # 将page对象渲染到文章页面，定义上一页、下一页、共有几页、当前第几页
        return render(request, 'backweb/article.html', {'page': page})


def del_article(request, num):
    """定义删除文章页面"""
    if request.method == 'GET':
        # 传入的第二个num参数是article.id 由此来删除文章
        Article.objects.filter(pk=num).delete()
        return HttpResponseRedirect(reverse('backweb:article'))


def add_article(request):
    """定义增加/修改文章页面"""
    if request.method == 'GET':
        return render(request, 'backweb/add_article.html')

    if request.method == 'POST':
        from backweb.artForm import AddArtForm
        form = AddArtForm(request.POST, request.FILES)
    # 验证成功就添加文章
    if form.is_valid():
        title = form.cleaned_data['title']
        describe = form.cleaned_data['describe']
        content = form.cleaned_data['content']
        tags = form.cleaned_data['tags']
        icon = form.cleaned_data['icon']

        t_name = form.cleaned_data['t_name']
        if ArticleType.objects.filter(t_name=t_name):
            type_id = ArticleType.objects.filter(t_name=t_name).first().id
        else:
            ArticleType.objects.create(t_name=t_name)
            type_id = ArticleType.objects.filter(t_name=t_name).first().id

        Article.objects.create(title=title,
                               describe=describe,
                               content=content,
                               tags=tags,
                               icon=icon,
                               type_id=type_id
                               )
        # 返回文章列表页面
        return HttpResponseRedirect(reverse('backweb:article'))
    else:
        errors = form.errors
        return render(request, 'backweb/add_article.html', {'errors': errors})


def edit_article(request, pk):
    """定义修改文章"""
    if request.method == 'GET':
        article = Article.objects.filter(pk=pk).first()
        return render(request, 'backweb/add_article.html', {'article': article})
    # POST请求修改文章数据
    if request.method == 'POST':
        from backweb.artForm import EditArtForm
        form = EditArtForm(request.POST, request.FILES)
        # 验证通过进行数据更改
        if form.is_valid():
            title = form.cleaned_data['title']
            describe = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            tags = form.cleaned_data['tags']
            icon = form.cleaned_data['icon']

            t_name = form.cleaned_data['t_name']
            if ArticleType.objects.filter(t_name=t_name):
                type_id = ArticleType.objects.filter(t_name=t_name).first().id
            else:
                ArticleType.objects.create(t_name=t_name)
                type_id = ArticleType.objects.filter(t_name=t_name).first().id

            article = Article.objects.filter(pk=pk).first()
            article.title = title
            article.describe = describe
            article.content = content
            article.tags = tags
            article.type_id = type_id
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            errors = form.errors
            article = Article.objects.filter(pk=pk).first()
            return render(request, 'backweb/add_article.html', {'errors': errors,
                                                                'article': article})


def show_article(request, pk):
    if request.method == 'GET':
        article = Article.objects.filter(pk=pk).first()
        if article:
            return render(request, 'backweb/show_article.html', {'article': article})
        else:
            err_show = '展示文章错误'
            return render(request, 'backweb/show_article.html', {'err_show': err_show})

def loginlog(request):
    """定义登录日志信息"""
    if request.method == 'GET':
        return render(request, 'backweb/loginlog.html')





