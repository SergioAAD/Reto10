from app.modules.modulesModel import ModulesModel
from flask import g


class ModulesController:
    def get_all(self):
        # fetch_all
        # fetch_one
        records = ModulesModel.query.filter_by(status=1).all() # first()
        g.modules = records
        print(records)