from flask import Blueprint
from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required
import time
demo = Blueprint('demo', __name__, url_prefix='/api/v1')


@demo.route("/demo", methods=['GET'])
# @jwt_required
def demo_test():
    demo_dict = {
        "one": 1,
        "two": 2,
    }
    return demo_dict
