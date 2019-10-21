# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 16:23
# @Author  : 何盛信
# @Email   : 2958029539@qq.com
# @File    : setup.py
# @Project : OverLoad
# @Software: PyCharm

from setuptools import setup, find_packages

setup(
    name="OverLoad",
    version='0.1',
    author="yiyexingyu",
    author_email="2958029539@qq.com",
    description=("实现python的重载",),
    license="GPLv3",
    keywords="python overload",
    packages=find_packages(),
    package_dir={'': '.'},
    zip_safe=False
)
