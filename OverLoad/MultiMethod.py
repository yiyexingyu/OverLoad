# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 15:14
# @Author  : 何盛信
# @Email   : 2958029539@qq.com
# @File    : MultiMethod.py
# @Project : OverLoad
# @Software: PyCharm
# 相关来源： https://www.artima.com/weblogs/viewpost.jsp?thread=101605

registry = {}


class MultiMethod(object):

    def __init__(self, name):
        self._name = name
        self._type_map_to_fun = {}

    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args)
        print("call function ", self._name, " ", types)
        function = self._type_map_to_fun.get(types)
        if not function:
            raise TypeError("no overload function found param list like ", list(types))
        return function(*args)

    def register(self, types, function):
        if types in self._type_map_to_fun:
            raise TypeError("redeclared function param list like ", list(types))
        self._type_map_to_fun[types] = function


def overload_obo(*types):
    def register(function):
        name = function.__name__
        multi_method = registry.get(name)

        if not multi_method:
            multi_method = registry[name] = MultiMethod(name)
        multi_method.register(types, function)
        return multi_method
    return register


def overload(*types):
    """可以堆叠式使用该修饰符，方便使用， 但是该方法线程不安全，虽然问题不大"""
    def register(function):
        """
        判断function 在之前有没有注册过（如果有属性__lastreg__说明注册过），如果注册过那么function就是一个
        MultiMethod实例， 而属性__lastreg__是源函数的id-------multi_method.__lastreg__ = function
        """
        function = getattr(function, "__lastreg__", function)
        name = function.__name__
        multi_method = registry.get(name)

        if not multi_method:
            multi_method = registry[name] = MultiMethod(name)
        multi_method.register(types, function)
        multi_method.__lastreg__ = function
        return multi_method
    return register


if __name__ == '__main__':

    @overload(int, int)
    def foo(a, b):
        print("int + int ", a + b)

    @overload()
    @overload(float)
    def foo(a=13.):
        print("float ", a)

    # 此时 (两个)foo其实是同一个MultiMethod实例
    # foo()会调用它的 __call__方法
    foo(12, 3)
    foo()
    foo(12.)
