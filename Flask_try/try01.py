
from flask import Flask
#导入配置文件
import config

#初始化Flask对象
#传递参数__name__
app = Flask(__name__)
app.config.from_object(config)

#装饰器@。。作为url与视图函数的映射
@app.route('/')
def hello_world():
    return '第一个flask程序32'


if __name__ == '__main__':
    #启动一个应用服务器接受用户请求
    #while True
    #   listen()
    app.run()
