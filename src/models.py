from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Family(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50),unique=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    lucky_numbers = db.Column(db.String(100), nullable=False)

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }