from app import db
from sqlalchemy.sql import func

class ModulesModel(db.Model):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)
    status = db.Column(db.Integer)

    menu = db.relationship('MenuModel', back_populates='modules')

    def __repr__(self):
        return f'Modules: {self.name}'
