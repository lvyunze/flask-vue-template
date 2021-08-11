from flask_jwt_extended import JWTManager
import logging
from logging import FileHandler
from flask_cors import CORS
from apps.routers import create_app
app = create_app()

if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('flask.log')
    app.logger.addHandler(handler)
    CORS(app)
    jwt = JWTManager(app)
    app.run()
