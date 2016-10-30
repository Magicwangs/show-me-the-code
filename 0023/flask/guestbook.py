# -*- coding: utf-8 -*-
# python2.7
# virtualenv: flask
# __author__: MagicWang

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
import time

# configuration配置
DATABASE = './tmp/guestbook.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# 创建实例
app = Flask(__name__)
#使用本模块的配置
app.config.from_object(__name__)
## 启用行语句
app.jinja_env.line_statement_prefix = '#'

# 连接数据库
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# 初始化数据库
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    #尝试获取g.b,如果不存在就是返回None,防止出错
    db = getattr(g, 'db', None)
    if db is None:
        db.close()
    g.db.close()

# 告诉Flask是什么样的URL触发我们的函数
@app.route('/')
def show_entries():
    cur = g.db.execute('select name,text,time from entries order by id desc')
    entries = [dict(name=row[0], text=row[1], time=row[2])
            for row in cur.fetchall()]
    for i in entries:
        print i
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    g.db.execute('insert into entries (name,text,time) values (?,?,?)',
                [request.form['name'],request.form['text'],current_time])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] is None:
            error = "Invalid username"
        else:
            session['logged_in'] = True
            session['name'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name, seq=['22','66'])

if __name__ == '__main__':
    # 第一次运行时初始化
    # init_db()
    # 监听所有IP，端口为8000，允许外网访问，windows需要关闭防火墙
    app.run(host='0.0.0.0', port=8000)
