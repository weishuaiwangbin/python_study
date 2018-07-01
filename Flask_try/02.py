from flask import Flask,url_for
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    print(url_for('my_list'))
    print(url_for('article',id='123'))
    return '第一个flask程序--首页'

@app.route('/list/')
def my_list():
    return 'list'

@app.route('/article/<id>')
def article(id):
    return u'您请求的参数是：%s' %id

if __name__ == '__main__':
    app.run()