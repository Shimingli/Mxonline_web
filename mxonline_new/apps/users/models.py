# coding:utf-8

from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。
# blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填
# http://www.weiguda.com/blog/8/


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default=u"")
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="female")
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y%m", default=u"image/default.png", max_length=100)
    # 因为图像在后台存储的时候是一个字符串形式，所以需要设置一个max_length参数.

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    # 关于Meta：https://www.chenshaowen.com/blog/the-django-model-meta/

    def __unicode__(self):
        return self.username

    def get_unread_nums(self):
        """
        获取用户未读消息数量
        :return:
        """
        from operation.models import UserMessage
        """
        这个引入不能放在开头
        """
        return UserMessage.objects.filter(user=self.id,has_read=False).count()


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(max_length=30, choices=(("register", u"注册"), ("forget", u"找回密码"), ("updata_email", u"修改邮箱")), verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")
    # datetime.now():default时间为EmailVerifyRecord编译时间
    # datetime.now：default时间为EmailVerifyRecord实例化时间

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return '{0}[{1}]'.format(self.code,self.email)

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(max_length=100, upload_to="banner/%Y%m", verbose_name=u"轮播图")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
