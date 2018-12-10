from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from backweb.models import Article, ArticleType

# Create your views here.
# 页面路由


def index(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-modify_time')
        return render(request, 'web/index.html', {'articles': articles})


def about(request):
    if request.method == 'GET':
        return render(request, 'web/about.html')


def gbook(request):
    if request.method == 'GET':
        return render(request, 'web/gbook.html')


def info(request, pk):
    if request.method == 'GET':
        art_type = ArticleType.objects.all()
        article = Article.objects.filter(pk=pk).first()
        if article.author_id:
            return render(request, 'web/info.html', {'article': article, 'art_type': art_type})
        else:
            article.author_id = 1
            return render(request, 'web/info.html', {'article': article, 'art_type': art_type})


def infopic(request):
    if request.method == 'GET':
        return render(request, 'web/infopic.html')


def share(request):
    if request.method == 'GET':
        return render(request, 'web/show_type.html')


def add_art(request):
    # 添加文章
    if request.method == 'GET':
        return render(request, 'web/add_art.html')

    from web.Artform import AddArtForm
    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)

    if form.is_valid():
        # 验证成功
        from backweb.models import Article
        title = form.cleaned_data['title']
        describe = form.cleaned_data['describe']
        content = form.cleaned_data['content']
        icon = form.cleaned_data['icon']
        Article.objects.create(title=title, describe=describe, content=content, icon=icon)

        # 创建成功后跳转文章列表页
        from django.http import HttpResponseRedirect
        from django.urls import reverse
        return HttpResponseRedirect(reverse('web:list'))
    else:
        # 表单验证失败，重新添加文章
        errors = form.errors
        return render(request, 'web/add_art.html', {'errors': errors})


def list_art(request):
    # 定义文章列表
    if request.method == 'GET':
        # 使用Django库Paginator
        from backweb.models import Article
        from django.core.paginator import Paginator
        # 得到所有文章
        articles = Article.objects.all()
        # 得到当前是第几页, 如果有page，就为page，否则为1
        page = int(request.GET.get('page', 1))
        # 按照每页6条分页
        paginator = Paginator(articles, 6)
        # 获取分页中的第几页对象
        page = paginator.page(page)
        # 获取文章类型
        art_type = ArticleType.objects.all()
        # 获取所有文章，便于显示标签云
        articles = Article.objects.all()
        # 在文章列表中定义上一页、下一页
        return render(request, 'web/list.html', {'page': page,
                                                 'art_type': art_type,
                                                 'articles': articles})
    if request.method == 'POST':
        from backweb.models import Article
        from django.core.paginator import Paginator
        content = request.POST.get('search')
        articles = Article.objects.filter(content__contains=content)

        page = int(request.GET.get('page', 1))
        # 按照每页6条分页
        paginator = Paginator(articles, 6)
        # 获取分页中的第几页对象
        page = paginator.page(page)
        # 获取文章类型
        art_type = ArticleType.objects.all()
        # 获取所有文章，便于显示标签云
        articles = Article.objects.all()
        # 在文章列表中定义上一页、下一页
        return render(request, 'web/list.html', {'page': page,
                                                 'art_type': art_type,
                                                 'articles': articles})




def show_type(request, pk):
    if request.method == 'GET':
        article = Article.objects.filter(type_id=pk)
        # 导入paginator
        from django.core.paginator import Paginator
        page = int(request.GET.get('page', 1))

        paginator = Paginator(article, 6)
        page = paginator.page(page)
        art_type = ArticleType.objects.all()
        articles = Article.objects.all()
        return render(request, 'web/show_type.html', {'page': page,
                                                      'art_type': art_type,
                                                      'articles': articles})

