from app import db
from sqlalchemy.sql import func


class MenuModel(db.Model):
    __tablename__ = 'menu' # flask migrate
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(50))
    icon = db.Column(db.String(60))
    status = db.Column(db.Integer)
    modules_id = db.Column(db.Integer, db.ForeignKey('modules.id'))

    modules = db.relationship('ModulesModel', uselist=False, back_populates='menu') # [{}] -> {}

    def __repr__(self):
        return f'Menu: {self.name}'
