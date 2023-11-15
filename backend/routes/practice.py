from flask import Blueprint

practice_blueprint = Blueprint('practice', __name__)

@practice_blueprint.route('/practice')
def practice():
    # ... practice logic ...
    pass