from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
# from flask.views import MethodView

app = Flask(__name__)

import mysql.connector
conn = mysql.connector.connect(user='root', password='x5', database='ironnotes')
cursor = conn.cursor()



@app.route('/')
def index():
    return 'Index Page'

# 传入参数
@app.route('/user/<username>/<int:post_id>')
def show_user_profile(username, post_id):
    # show the user profile for that user
    return f'User {escape(username)} {post_id}'


@app.route('/User/<opreation>', methods=['GET', 'POST'])
def User(opreation):
    if opreation == 'check':
        print('检查是否为已经注册过的用户/检测用户名是否可用【Get】')
        userId = request.args.get('userId')
        cursor.execute('SELECT * FROM user WHERE userId = %s', (userId,))
        values = cursor.fetchall()
        if values == [] :
            res = 'available'
        else:
            res = 'unAvailable'
    elif opreation == 'regist':
        print('注册新用户【Post】')
        # cursor.execute('SELECT count(name) FROM user')
        count = int(cursor.fetchall()[0][0]) + 1
        print(count)
        wxid = request.args.get('wxid')
        name = '小土豆'+ str(count)
        avatar = request.args.get('avatar')
        flower = request.args.get('flower')
        # cursor.execute('INSERT INTO user (wxid, name, avatar, flower) values (%s, %s, %s, %s)', (wxid, name, avatar, flower))
        # conn.commit()
        res = name # 将初始用户名返回至小程序端缓存
    elif opreation == 'changeInfo':
        print('修改用户信息')
        wxid = request.args.get('wxid')
        name = request.args.get('name')
        motto = request.args.get('motto')
        # cursor.execute('UPDATE user SET name = %s,motto = %s WHERE wxid = %s', (name, motto, wxid))
        # conn.commit()
        print(wxid, name, motto)
        res = 'Changed'
    return res
    # return