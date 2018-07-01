from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    class Person(object):
        name = '黄勇'
        age = 18
    p = Person()

    context = {
        'username' : 'weishuai',
        'gender' : '男',
        'age' : 18,
        'person' : p,
        'website':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }
    return render_template('index.html',**context)

if __name__ == '__main__':
    app.run(debug=True)