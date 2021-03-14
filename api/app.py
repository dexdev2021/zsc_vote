# coding=utf-8

from flask import Flask, jsonify, request
import pymysql
from flaskext.mysql import MySQL


app = Flask(__name__)
app.debug = True   

conn = MySQL(
    app, 
    host="localhost", 
    user="root", 
    password="123456",
    db="vote", 
    autocommit=True, 
    cursorclass=pymysql.cursors.DictCursor,
)


@app.route('/v1')
def hello_world():
    return 'Hello, World!'


@app.route('/v1/node_list')
def node_list():
    addr = request.args.get('addr')
    sql = """SELECT n.node_name, n.node_address, n.node_logo, n.node_amount, v.nv_id, v.vote_address, v.vote_amount
        from zsc_node n 
        LEFT JOIN zsc_node_vote v on n.node_id=v.node_id 
            and v.vote_address='{0}' ORDER BY node_amount DESC LIMIT 21""".format(addr)
    cursor = conn.get_db().cursor()
    cursor.execute(sql)
    nodes = cursor.fetchall()
    return jsonify({"code":200, "list": nodes})


if __name__ == '__main__':
    app.debug = True
    app.run()