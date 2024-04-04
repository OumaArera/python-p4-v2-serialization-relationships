from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Zookeeper(db.Model, SerializerMixin):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)

    animals = db.relationship('Animal', backref='zookeeper')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Enclosure(db.Model, SerializerMixin):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship('Animal', backref='enclosure')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Animal(db.Model, SerializerMixin):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
