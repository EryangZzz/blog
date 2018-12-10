"""__author__ = ErYang"""
from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=2,
                            required=True,
                            error_messages={
                                'required': '文章标题必填',
                                'min_length': '不小于2个字符'
                            })
    describe = forms.CharField(min_length=5,
                               required=True,
                               error_messages={
                                   'required': '文章描述必填',
                                   'min_length': '不少于5个字符'
                               })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必填',
                              })
    tags = forms.CharField(required=True,
                           min_length=2,
                           error_messages={
                               'required': '文章标签必填',
                               'min_length': '文章标签不少于2个字符'
                           })
    t_name = forms.CharField(required=True,
                             error_messages={
                                 'required': '文章分类名必填'
                             })
    icon = forms.ImageField(required=True,
                            error_messages={
                                'required': '首图必填',
                            }
                            )


class EditArtForm(forms.Form):
    title = forms.CharField(min_length=2,
                            required=True,
                            error_messages={
                                'required': '文章标题修改后必填',
                                'min_length': '不小于2个字符'
                            })
    describe = forms.CharField(min_length=5,
                               required=True,
                               error_messages={
                                   'required': '文章描述修改后必填',
                                   'min_length': '不少于5个字符'
                               })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容修改后必填',
                              })
    tags = forms.CharField(required=True,
                           min_length=2,
                           error_messages={
                               'required': '文章标签必填',
                               'min_length': '文章标签不少于2个字符'
                           })
    t_name = forms.CharField(required=True,
                             error_messages={
                                 'required': '文章分类名必填'
                             })
    icon = forms.ImageField(required=False)

