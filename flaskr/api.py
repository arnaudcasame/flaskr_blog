from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/users')
def index():
    db = get_db()
    users_list=[]
    users = db.execute(
        'SELECT *'
        ' FROM user '
        ' ORDER BY id DESC'
    ).fetchall()
    for user in users:
        users_list.append({
            'id': user['id'],
            'username': user['username'],
            'password': user['password']})
    return jsonify(users_list)
