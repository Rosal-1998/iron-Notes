from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page2'

@app.route('/test')
def test():
    return 'test, World'

# 传入参数
@app.route('/user/<username>/<int:post_id>')
def show_user_profile(username,post_id):
    # show the user profile for that user
    return f'User {escape(username)} {post_id}'

# 传入数字参数
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

# 传入路径
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/login')
def login():
    return 'login222'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
def do_the_login():
    return 'login'