from flask import request, Blueprint, jsonify
from SRRMSv2.models.userModel import User
import uuid
import datetime
from SRRMSv2.models.userModel import db

userBP = Blueprint('userApi', __name__)

@userBP.route('/add', methods=['GET', 'POST'])
def useraction():
    db.create_all()
    if request.method == 'POST':
        data = request.json
        return save_new_user(data=data)
    elif request.method == 'GET':
        return get_all_users()


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except:
            response_object = {
                'status': 'fail',
                'message': 'Problem occured in db',
            }
            return jsonify(response_object), 401

        finally:
            response_object = {
                'status': 'Ok',
                'message': 'User Created Successful',
            }
            return jsonify(response_object), 200

    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return jsonify(response_object), 409


def get_all_users():
    response_object = {
        'status': 'success',
        'data': User.query.first()
    }
    return jsonify(response_object), 200

