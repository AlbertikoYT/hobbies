from flask import Flask, render_template, request, redirect, url_for, jsonify
import models as dbase
from member import Member
from hobby import Hobby
from membership import Membership
from bson.objectid import ObjectId

app = Flask(__name__)
db = dbase.dbConnection()

@app.route('/')
def index():
    memberships = db['memberships'].find()
    members = {str(m['_id']): f"{m['first_name']} {m['last_name']}" for m in db['members'].find()}
    hobbies = {h['hobby_code']: h['hobby_description'] for h in db['hobbies'].find()}
    return render_template('index.html', memberships=memberships, members=members, hobbies=hobbies)

@app.route('/add_membership', methods=['GET', 'POST'])
def add_membership():
    if request.method == 'POST':
        member_id = request.form['member_id']
        hobby_code = request.form['hobby_code']
        percentage = int(request.form['percentage'])
        level = request.form['level_of_ability']

        new_entry = Membership(member_id, hobby_code, percentage, level)
        db['memberships'].insert_one(new_entry.toDBCollection())
        return redirect(url_for('index'))

    members = list(db['members'].find())
    hobbies = list(db['hobbies'].find())
    return render_template('add_hobby.html', members=members, hobbies=hobbies)

@app.errorhandler(404)
def notFound(error=None):
    return jsonify({'message': 'No encontrado ' + request.url, 'status': '404 Not Found'}), 404

if __name__ == '__main__':
    app.run('0.0.0.0', 777, debug=True)
