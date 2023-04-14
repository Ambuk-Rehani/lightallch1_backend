from flask import *
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
api = Flask(__name__)
CORS(api)

api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(api)


class Count(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)
    

@api.route('/profile', methods = ['GET', 'POST'])
def my_profile():
    count_record = Count.query.filter_by(id=1).first()
    if count_record is None:
        count_record = Count(id=1, count=0)
        db.session.add(count_record)
        db.session.commit()
        
    if request.method == 'POST':
        data = request.get_json()
        count_val = data['count']
        count_record.count = count_val
        db.session.commit()
        response_body = {"count": count_val}
        return response_body
    else:
        count_val = count_record.count
        response_body = {
            "name": "Nagato",
            "about" :"Hello! I'm a full stack developer that loves python and javascript",
            "count" : count_val
        }
        return response_body


def getCount():
    return count_val
    