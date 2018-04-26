# coding:utf-8

__Author__ = 'eyu Fanne'
__Date__ = '2017/7/16'

import re
from django import forms
from operation.models import UserAsk


# 使用modelform编写表单
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ["name", "mobile", "course_name"]
    """
    验证手机号码是否合法
    """
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
