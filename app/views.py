from flask import render_template
from .app import app


@app.route('/')
def index():
    love='milcah'
    return render_template('index.html', love=love)



#     db = SQLAlchemy()

# def create_app(config):
#     app = Flask(__name__)
#     db.init_app(app)

#     adm = Admin(app,name='flaskadmin')
#     from app.models import User
#     adm.add_view(ModelView(User, db.session))
#     return app
