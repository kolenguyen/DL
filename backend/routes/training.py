from flask import Blueprint

training_blueprint = Blueprint('training', __name__)

@training_blueprint.route('/training')
def training():
    # ... training logic ...
    pass