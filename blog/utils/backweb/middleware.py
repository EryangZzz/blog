"""__author__ = ErYang"""
from django.utils.deprecation import MiddlewareMixin
from backweb.models import User
from django.http import HttpResponseRedirect
from re import match


# 定义中间件实现登录验证


class loginStatusMiddleware(MiddlewareMixin):
    # 定义网页请求时的判断
    def process_request(self, request):
        # 1.如果是访问注册和登录页面不需要验证

        if match(r'/web/', request.path) or \
                match(r'/$', request.path) or \
                request.path in ['/backweb/login/', '/backweb/register/']:
            return None

        # 2.取得session中存入的键值对
        user_id = request.session.get('user_id')
        # 如果存在user_id,则拿到数据库用户，将用户赋值给request.user
        if user_id:
            user = User.objects.filter(pk=user_id).first()
            if user:
                request.user = user
                return None
            else:
                return HttpResponseRedirect('/backweb/login/')

        return HttpResponseRedirect('/backweb/login/')

