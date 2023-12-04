from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

# from .usemodels.user import User
from .models.user import User
ma = Marshmallow()

class UserSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        # load_instance = True
        
    # id = auto_field()
    # username = auto_field()
    # emal = auto_field()
    # password = auto_field()
    # createdate = auto_field()