# /usr/bin/python
# coding:utf-8




from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import DEFAULT_FROM_EMAIL


# def random_str(randomlength=8):
#     '''
#     生成随机字符串
#     '''
#     str = ''
#     chars = 'AaBbCcDdEeFfGgHhJjIi234567890'
#     length = len(chars)-1
#     print length
#     random = Random
#     for i in range(randomlength):
#         str+=chars[random.randint(0,length)]
#     return str

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def send_register_email(email,send_type="register"):
    email_recod = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_recod.code = code
    email_recod.email = email
    email_recod.send_type = send_type
    email_recod.save()

    email_title = ""
    email_body = ""
    if send_type == "register":
        email_title = "注册激活"
        email_body = "请点击激活：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "重置密码"
        email_body = "请点击重置密码：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email])
        if send_status:
            pass
    elif send_type == "updata_email":
        email_title == "邮箱修改验证码"
        email_body = "你的邮箱验证码为：{0}".format(code)
        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email])
        if send_status:
            pass








