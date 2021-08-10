from flask import Flask
from setting import DevelopmentConfig
from apps.routers.login import login
from apps.routers.demo import demo


def create_app():
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(DevelopmentConfig)
    # 注册蓝图
    app.register_blueprint(login)
    app.register_blueprint(demo)
    return app
