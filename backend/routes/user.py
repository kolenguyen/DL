from flask import Blueprint

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user/profile')
def user_profile():
    # ... user profile logic ...
    pass