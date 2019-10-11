# -*- coding: utf-8 -*-
# @Time    :2019/10/11 11:06 PM
# @Author  : wangqiao


__all__ = ['log_register', 'RequestFormatter']

import logging
from flask import request


def log_register(config) -> None:
    """
    默认的日志配置
    """
    import os
    from logging.config import dictConfig
    log_dir = config.LOG_DIR
    dir_path = os.path.join(log_dir, config.PROJECT_NAME)
    log_path = os.path.join(dir_path, 'now.log')

    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': config.LOG_FORMAT,
                'class': 'utils.log.RequestFormatter'
            }
        },
        'handlers': {
            'default': {
                'level': config.LOG_LEVEL,
                'filename': log_path,
                'formatter': 'default',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'when': config.LOG_SPLIT_UNIT,
                'interval': config.LOG_SPLIT_INTERVAL,
            }
        },
        'root': {
            'level': 'INFO',
            'handlers': ['default']
        }
    })


class RequestFormatter(logging.Formatter):
    """
    flask请求信息log打印格式化处理器
    """

    def format(self, record: logging.LogRecord) -> str:
        try:
            setattr(record, 'url', request.url)
            setattr(record, 'remoteaddr', request.remote_addr)
        except RuntimeError:
            setattr(record, 'url', 'no')
            setattr(record, 'remoteaddr', 'no')
        return super(RequestFormatter, self).format(record)
