import MySQLdb.cursors
import flask
import functools
import hashlib
import math
import os
import pathlib
import random
import string
import tempfile
import time


static_folder = pathlib.Path(__file__).resolve().parent.parent / 'public'
icons_folder = static_folder / 'icons'
app = flask.Flask(__name__, static_folder=str(static_folder), static_url_path='')
app.secret_key = 'tonymoris'
avatar_max_size = 1 * 1024 * 1024

if not os.path.exists(str(icons_folder)):
    os.makedirs(str(icons_folder))

config = {
    'db_host': os.environ.get('ISUBATA_DB_HOST', 'localhost'),
    'db_port': int(os.environ.get('ISUBATA_DB_PORT', '3306')),
    'db_user': os.environ.get('ISUBATA_DB_USER', 'root'),
    'db_password': os.environ.get('ISUBATA_DB_PASSWORD', ''),
}


def dbh():
    #if hasattr(flask.g, 'db'):
    #    return flask.g.db

    db = MySQLdb.connect(
        host   = config['db_host'],
        port   = config['db_port'],
        user   = config['db_user'],
        passwd = config['db_password'],
        db     = 'isubata',
        charset= 'utf8mb4',
        cursorclass= MySQLdb.cursors.DictCursor,
        autocommit = True,
    )
    cur = db.cursor()
    cur.execute("SET SESSION sql_mode='TRADITIONAL,NO_AUTO_VALUE_ON_ZERO,ONLY_FULL_GROUP_BY'")
    return db


def save_image():
    cur = dbh().cursor()
    #cur.execute("SELECT * FROM image WHERE name = %s", (file_name,))
    cur.execute("SELECT * FROM image")
    rows = cur.fetchall()
    for i, row in enumerate(rows): 
        print(i)
        print(os.path.join('icons', row['name']))
        with open(os.path.join('icons', row['name']), 'wb') as f:
            f.write(row['data'])
    #if row and mime:
    #    return flask.Response(row['data'], mimetype=mime)
    #flask.abort(404)

if __name__ == "__main__":
    save_image()
    #app.run(port=8080, debug=True, threaded=True)
