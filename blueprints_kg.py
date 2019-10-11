# -*- coding: utf-8 -*-
# @Time    :2019/10/11 11:17 PM
# @Author  : wangqiao


__all__ = ['blueprint_register']

from flask import Flask


def blueprint_register(app: Flask) -> None:
    """
    蓝图注册函数
    """

    # api文档
    from views.hello import HelloView
    app.add_url_rule(
        '/hello/',
        view_func=HelloView.as_view(name='hello')
    )




