from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from apps.models.users import Users

login = Blueprint('login_bp', __name__, url_prefix='/api/v1')


# 用户登录
@login.route('/login', methods=['POST'])
def user_login():
    username = request.json['username']
    password = request.json['password']
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    user = Users.get_or_none(Users.username == username, Users.password == password)
    if user is None:
        return jsonify({'success': False, 'message': 'Bad username or password'}), 401
    access_token = create_access_token(identity=username)
    return jsonify({'success': True, 'token': access_token}), 200


# 管理员登录
@login.route('/verify-token', methods=['POST'])
@jwt_required
def verify_token():
    return jsonify({'success': True}), 200


# 获取用户信息
@login.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify({"name": current_user}), 200


# 注销登录
@login.route('/logout', methods=['POST'])
@jwt_required
def logout():
    return jsonify({"code": 200, "status": "success"}), 200
