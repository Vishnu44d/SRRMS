from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from SRRMSv2.models import db
from SRRMSv2.api import statusBP, testBP, userBP


app = Flask(__name__)
Migrate(app, db)

with app.app_context():
    db.init_app(app)

app.register_blueprint(statusBP, url_prefix='/status')
app.register_blueprint(testBP, url_prefix='/test')
app.register_blueprint(userBP, url_prefix='/user')

if __name__ == "__main__":
    app.run(debug=True)
