# !/usr/bin/env python
# coding:utf-8
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


'''
一些注释信息
管理员账号密码：
root,qwe123QAZ
'''