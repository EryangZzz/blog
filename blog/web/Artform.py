"""__author__ = ErYang"""
from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=5, required=True,
                            error_messages={
                                'required': '文章标题不能为空',
                                'min_length': '文章标题至少5个字符'
                            })
    describe = forms.CharField(min_length=2, required=True,
                               error_messages={
                                   'required': '文章描写不能为空',
                                   'min_length': '文章描述至少2个字符'
                               })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容不能为空'
                              })

    icon = forms.ImageField(required=True, error_messages={
        'required': '首图必填'
    })
    
 