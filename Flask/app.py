from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask_cors import CORS
# from flask.views import MethodView

from datetime import datetime



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

# 更新Contributions
def updateContributions(learnrecordid,learnrecordpersonid):
    # 格式：2024-02-26 --> 240226
    date_formatted = datetime.fromtimestamp(int(learnrecordid)).strftime('%y%m%d')
    cursor.execute('SELECT * FROM contributions WHERE personid = %s and date = %s', (learnrecordpersonid,date_formatted))
    values = cursor.fetchall()
    if values == []:
        # 添加contributions
        cursor.execute('INSERT INTO contributions (personid, date, times) values (%s, %s, %s)', (learnrecordpersonid, date_formatted, 1))
        conn.commit()
    else:
        # 修改contributions
        cursor.execute('UPDATE contributions SET times = times + 1 WHERE personid =%s AND date = %s ', (learnrecordpersonid, date_formatted))
        conn.commit()
    return 'UpdateContributions'




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
        updateContributions(learnrecordid,learnrecordpersonid)
        res = 'addSuccess'
    elif opreation == 'delete':
        print('删除学习记录【Get】')
        learnrecordid = request.args.get('learnrecordid')
        cursor.execute('DELETE FROM learnrecords WHERE learnrecordid = %s', (learnrecordid,))
        conn.commit()
        res = 'deleteSuccess'
    elif opreation == 'showInfo':
        print('查看学习记录【Get】')
        learnrecordpersonid = request.args.get('userId')
        cursor.execute('SELECT * FROM learnrecords WHERE learnrecordpersonid = %s', (learnrecordpersonid,))
        rows = cursor.fetchall()
        values = [{'learnrecordid': row[0], 'learnrecordcontent': row[1],'learnrecordpersonid':row[2]} for row in rows]
        print(values)
        res = values
    return res


@app.route('/Contributions/<opreation>', methods=['GET', 'POST'])
def Contributions(opreation):
    if opreation == 'showInfo':
        print('拉取本月贡献【Get】')
        personid = request.args.get('userId')
        date = request.args.get('date')
        cursor.execute('SELECT * FROM contributions WHERE personid = %s and date Like %s', (personid,date+'%'))
        rows = cursor.fetchall()
        values = [{'personid': row[0], 'date': row[1],'times':row[2]} for row in rows]
        print(values)
        res = values
    elif opreation == 'delete':
        print('删除学习记录【Get】')
        learnrecordid = request.args.get('learnrecordid')
        cursor.execute('DELETE FROM learnrecords WHERE learnrecordid = %s', (learnrecordid,))
        conn.commit()
        res = 'deleteSuccess'
    return res

# 知识库模块
@app.route('/Knowledge/<opreation>', methods=['GET', 'POST'])
def Knowledge(opreation):
    if opreation == 'add':
        print('添加知识库【GET】')
        userId = request.args.get('userId')
        knowledgeName = request.args.get('knowledgeName')
        description = request.args.get('description')
        cursor.execute('INSERT INTO knowledge (knowledgeId,userId, knowledgeName,description) values (UUID(), %s, %s,%s)', (userId, knowledgeName,description))
        conn.commit()
        res = 'addSuccess'
    elif opreation == 'showInfo':
        print('拉取用户知识库【Get】')
        userId = request.args.get('userId')
        cursor.execute('SELECT * FROM knowledge WHERE userId = %s', (userId,))
        rows = cursor.fetchall()
        print(rows)
        values = [{'userId': row[0], 'knowledgeId': row[1],'knowledgeName':row[2],'detail':row[3],'description':row[4]} for row in rows]
        print(values)
        res = values
    elif opreation == 'showDetail':
        print('拉取知识库详情【Get】')
        knowledgeId = request.args.get('knowledgeId')
        cursor.execute('SELECT * FROM knowledge WHERE knowledgeId = %s', (knowledgeId,))
        rows = cursor.fetchall()
        print(rows)
        values = [{'userId': row[0], 'knowledgeId': row[1],'knowledgeName':row[2],'detail':row[3],'description':row[4]} for row in rows]
        print(values)
        res = values
    elif opreation == 'updateDetail':
        print('修改知识库详情【Get】')
        knowledgeId = request.args.get('knowledgeId')
        detail = request.args.get('detail')
        cursor.execute('UPDATE knowledge SET detail = %s WHERE knowledgeId = %s', (detail, knowledgeId))
        conn.commit()
        res = 'updateDetailSuccess'
    return res
