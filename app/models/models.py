import datetime
from ..extends import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(50))
	password = db.Column(db.String(255))
	role = db.Column(db.String(20), default='')
	create_time = db.Column(db.DateTime, default=datetime.datetime.now)
	is_active = db.Column(db.Boolean, default=False)
	token = db.Column(db.String(20). default='')
	