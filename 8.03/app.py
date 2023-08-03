from flask import Flask, render_template, jsonify, request
import pymysql

app = Flask(__name__)

# 메인화면
@app.route('/')
def main():
    db = pymysql.connect(
        host='gotiger.ipdisk.co.kr',
        port=3316,
        user='nipa',
        password='1234',
        database='nipa',
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )
    with db:
        curs = db.cursor()
        sql = f'select * from `users`'
        curs.execute(sql)
        result = curs.fetchall()

    return render_template('index.html', result=result)


# insert
@app.route('/insert', methods=['POST'])
def insert():
    nickname = request.get_json()['nickname']
    email = request.get_json()['email']
    password = request.get_json()['password']

    db = pymysql.connect(
        host='gotiger.ipdisk.co.kr',
        port=3316,
        user='nipa',
        password='1234',
        database='nipa',
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )
    with db:
        curs = db.cursor()
        sql_insert = f'INSERT INTO `users` (nickname, email, password) VALUES("{nickname}", "{email}", "{password}");'
        curs.execute(sql_insert)

    return jsonify({'msg': 'Insert 완료'})

# insert
@app.route('/select', methods=['POST'])
def select():
    nickname = request.get_json()['nickname']
    password = request.get_json()['password']

    db = pymysql.connect(
        host='gotiger.ipdisk.co.kr',
        port=3316,
        user='nipa',
        password='1234',
        database='nipa',
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )
    with db:
        curs = db.cursor()
        sql_select = f'select id, nickname, email, password from `users` where nickname = "{nickname}" or password = "{password}" ;'
        curs.execute(sql_select)
        result = curs.fetchall()

    return jsonify({'data': result})

if __name__ == '__main__':
    app.run(debug=True)