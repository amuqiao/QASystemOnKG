# -*- coding: utf-8 -*-
# @Time    :2019/10/11 11:03 PM
# @Author  : wangqiao


from typing import Any


def get_config(config_path: str) -> Any:
    """
    通过dot path获取config模块
    """
    from werkzeug.utils import import_string
    return import_string(config_path)
