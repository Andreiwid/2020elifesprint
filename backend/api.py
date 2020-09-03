from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    url_for,
    jsonify,
)
import sqlite3

app = Flask(__name__)

DATABASE = 'dataportals.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()     


@app.route('/dataportals/', methods=['GET'])
def dataportals():
    db = get_db()
    data = db.execute('SELECT * FROM datasets').fetchall()

    return jsonify(data)


@app.route('/dataportals/<year>/<month>/', methods=['GET'])
def dataportals_by_year_month(year=None, month=None):
    db = get_db()
    data = db.execute('SELECT * FROM datasets WHERE year = ? and month = ?', [year, month]).fetchall()

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)