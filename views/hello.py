# -*- coding: utf-8 -*-
# @Time    :2019/10/11 11:21 PM
# @Author  : wangqiao


__all__ = ['HelloView']

from flask import jsonify, Response
from flask.views import MethodView


class HelloView(MethodView):
    permissions = ['get']

    def get(self) -> Response:
        """
        测试
        """
        return jsonify('Hello World!')

