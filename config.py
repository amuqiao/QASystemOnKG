# -*- coding: utf-8 -*-
# @Time    :2019/10/11 11:07 PM
# @Author  : wangqiao


# ---------- flask config ----------

import os
import logging
from urllib.parse import quote



# 项目运行所处的环境,默认为'production'
# 可通过环境变量名FLASK_ENV配置
# 若FLASK_ENV存在,则通过配置文件所设置的ENV可能会无效
ENV = 'production'  # otherwise: 'development'

# 项目的DEBUG模式
# 当DEBUG为True时,项目会在代码更新的时候自动重启项目
# 若DEBUG为True时,页面会打印未能捕获的错误信息
# 若ENV为'development',则DEBUG默认为True,否则为False
DEBUG = False

# 项目的测试模式
# 若TESTING为True,则根应用验证直接通过
# 若TESTING为True,则csrf验证直接通过
# 若TESTING为True,则验证码验证直接通过
# 若TESTING为True,则接口访问次数不做限制
# 若TESTING为True时,错误不会被项目的内置捕获器所捕获,同时扩展插件也会更改他们的捕获行为以方便测试
TESTING = True

# 项目目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 项目名称
PROJECT_NAME = os.path.dirname(os.path.abspath(__file__)).split('/')[-1]

# 视图根路由, 必须包含blueprint_register函数
# 通过环境变量BLUEPRINTS参数传入
ROOT_BLUEPRINTS = os.environ.get('BLUEPRINTS_KG', 'blueprints_kg').split(';')

# ----- log config -----
# log文件所在位置,必须为绝对路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 日志的记录等级
LOG_LEVEL = logging.INFO

# 创建日志时,自动日志切分的周期单位,可为S-秒/M-分/H-时/D-天/midnight-半夜/W{0-6}-星期,从星期一开始
LOG_SPLIT_UNIT = 'midnight'

# 日志自动轮询的周期间隔
LOG_SPLIT_INTERVAL = 1

# 日志打印格式
# %(levelno)s: 打印日志级别的数值
# %(levelname)s: 打印日志级别名称
# %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s: 打印当前执行程序名
# %(funcName)s: 打印日志的当前函数
# %(lineno)d: 打印日志的当前行号
# %(asctime)s: 打印日志的时间
# %(thread)d: 打印线程ID
# %(threadName)s: 打印线程名称
# %(process)d: 打印进程ID
# %(message)s: 打印日志信息
# %(url)s: 打印日志时,请求的url地址
# %(remoteaddr)s: 打印日志时,请求的原始地址
LOG_FORMAT = '[%(levelname)s] %(asctime)s %(pathname)s[line:%(lineno)d] ip:%(remoteaddr)s access:%(url)s %(message)s'

