from app import app


# Modelos
from app.menu import menuModel
## Relaciones
### Debe respetarse la jerarquia de los modelos
### Ejm: El modelo usuario, se relaciona con Rol (UserModel -> rol_id <- RolesModel)
from app.roles import rolesModel
from app.user import userModel
from app.categories import categoriesModel
from app.tax import taxModel
from app.salesType import salesTypeModel
from app.modules import modulesModel
from app.product import productModel

## Rutas
from app.menu import menuRouter
from app.auth import authRouter
from app.home import homeRouter
from app.categories import categoriesRouter
from app.tax import taxRouter
from app.salesType import salesTypeRouter
from app.product import productRouter

# from app.modules import modulesRouter