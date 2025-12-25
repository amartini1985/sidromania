from flask import Flask, render_template, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, )
db = SQLAlchemy(app)
migrate = Migrate(db, app)

@app.route('/')
def index():
    return render_template_string('Все хорошо')

if __name__ == '__main__':
    app.run(debug=True, port=8000)