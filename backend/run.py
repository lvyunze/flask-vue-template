from flask_jwt_extended import JWTManager
import logging
from flask_cors import CORS
from apps.routers import create_app
from logging.handlers import TimedRotatingFileHandler
app = create_app()

if __name__ == '__main__':
    app.debug = True
    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
    handler = TimedRotatingFileHandler(
        "flask.log", when="D", interval=1, backupCount=15,
        encoding="UTF-8", delay=False, utc=True)
    app.logger.addHandler(handler)
    handler.setFormatter(formatter)
    CORS(app)
    jwt = JWTManager(app)
    app.run()
