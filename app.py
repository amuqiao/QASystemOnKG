# -*- coding: utf-8 -*-
# @Time    :2019/10/11 11:04 PM
# @Author  : wangqiao


__all__ = ['create_app', 'app']

from flask import Flask


def create_app() -> Flask:
    """
    flask实例化
    """
    import os
    from werkzeug.contrib.fixers import ProxyFix
    from utils import get_config
    from utils.log import log_register

    # 获取配置
    project_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.environ.get(f'{project_name.upper()}_CONFIG') or 'config'
    config = get_config(config_path)
    config.PROJECT_NAME = project_name
    # 配置日志系统
    log_register(config)

    instance = Flask(
        __name__,
        static_folder=getattr(config, 'STATIC_PATH', 'static'),
        static_url_path=getattr(config, 'STATIC_URL', None)
    )
    with instance.app_context():
        # 加载配置文件
        instance.config.from_object(config)

        # 注册蓝图
        for name in config.ROOT_BLUEPRINTS:
            blueprints = get_config(name)
            blueprints.blueprint_register(instance)

        return instance


# 实例化项目
app = create_app()

