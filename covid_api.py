from flask import Flask, jsonify, g, request, json
from sqlite3 import dbapi2 as sqlite3
DATABASE = 'C:/Users/Marshall/Documents/Webpage Project/projDB.db'
app = Flask(__name__)

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
		db.row_factory = sqlite3.Row
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None: db.close()

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

def find_state(name=''):
    sql = "select * from prison where state = '%s' limit 50" %(name)
    print(sql)
    db = get_db()
    rv = db.execute(sql)
    res = rv.fetchall()
    rv.close()
    #print(res[0])
    return res


@app.route('/')
def users():
	return jsonify(hello='world')

@app.route('/find_state/<string:name>', methods=['GET'])
def find_state_by_name(name):
    state = find_state(name)
    arr = []
    for i in range(len(state)):
        arr.append({'cfname' : state[i]['Canonical Facility Name'], 'state' : state[i]['State'], 'posPop' : state[i]['Pop Tested Positive'], 'deathPop' : state[i]['Pop Deaths'], 'posStaff' : state[i]['Staff Tested Positive'], 'deathStaff' : state[i]['Staff Deaths']})

    return jsonify(arr)

if __name__ == '__main__' : app.run(debug=True)