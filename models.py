from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import create_app
app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://Anand:AnandSql@localhost:5432/cars_api"
db = SQLAlchemy(app)
migrate = Migrate(app,db)
