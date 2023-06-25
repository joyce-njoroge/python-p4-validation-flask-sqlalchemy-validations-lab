from flask import Flask, make_response
from flask_migrate import Migrate
from sqlalchemy import exc

from models import db, Author, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

def do_execute(self, cursor, statement, parameters, context=None):
    try:
        cursor.execute(statement, parameters)
    except exc.IntegrityError as e:
        raise e.orig

@app.route('/')
def index():
    return 'Validations lab'

if __name__ == '__main__':
    app.run(port=5555, debug=True)