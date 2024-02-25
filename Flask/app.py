from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask_cors import CORS
# from flask.views import MethodView

app = Flask(__name__)
CORS(app, resources=r'/*')
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
    print('------',opreation)
    if opreation == 'check':
        print('检查是否为已经注册过的用户/检测用户名是否可用【Get】')
        userId = request.args.get('userId')
        cursor.execute('SELECT * FROM user WHERE userId = %s', (userId,))
        values = cursor.fetchall()
        if values == [] :
            res = 'available'
        else:
            res = 'unAvailable'
    elif opreation == 'login':
        print('登录【POST】')
        userId = request.args.get('username')
        password = request.args.get('password')
        print(userId,password)
        cursor.execute('SELECT password FROM user WHERE userId = %s', (userId,))
        values = cursor.fetchall()
        print(values[0][0])
        if values[0][0] == password :
            res = 'loginSuccess'
        else:
            res = 'loginFail'
    # elif opreation == 'regist':
    #     print('注册新用户【Post】')
    #     # cursor.execute('SELECT count(name) FROM user')
    #     count = int(cursor.fetchall()[0][0]) + 1
    #     print(count)
    #     wxid = request.args.get('wxid')
    #     name = '小土豆'+ str(count)
    #     avatar = request.args.get('avatar')
    #     flower = request.args.get('flower')
    #     # cursor.execute('INSERT INTO user (wxid, name, avatar, flower) values (%s, %s, %s, %s)', (wxid, name, avatar, flower))
    #     # conn.commit()
    #     res = name # 将初始用户名返回至小程序端缓存
    # elif opreation == 'changeInfo':
    #     print('修改用户信息')
    #     wxid = request.args.get('wxid')
    #     name = request.args.get('name')
    #     motto = request.args.get('motto')
    #     # cursor.execute('UPDATE user SET name = %s,motto = %s WHERE wxid = %s', (name, motto, wxid))
    #     # conn.commit()
    #     print(wxid, name, motto)
    #     res = 'Changed'
    
    return res
    # return


@app.route('/LearnRecord/<opreation>', methods=['GET', 'POST'])
def LearnRecord(opreation):
    if opreation == 'add':
        print('添加学习记录【GET】')
        learnrecordid = request.args.get('time')
        learnrecordcontent = request.args.get('content')
        learnrecordpersonid = request.args.get('userId')
        cursor.execute('INSERT INTO learnrecords (learnrecordid, learnrecordcontent, learnrecordpersonid) values (%s, %s, %s)', (learnrecordid, learnrecordcontent, learnrecordpersonid))
        conn.commit()
        res = 'addSuccess'
    elif opreation == 'showInfo':
        print('查看学习记录【Get】')
        learnrecordpersonid = request.args.get('userId')
        cursor.execute('SELECT * FROM learnrecords WHERE learnrecordpersonid = %s', (learnrecordpersonid,))
        rows = cursor.fetchall()
        values = [{'learnrecordid': row[0], 'learnrecordcontent': row[1],'learnrecordpersonid':row[2]} for row in rows]
        print(values)
        res = values
    return res
    # return


