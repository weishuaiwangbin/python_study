#利用time延时函数，生成两个函数
#利用多线程调用
#计算总运行时间
#练习带参数的多线程启动方法

import time
#导入多线程包并更名thread

import threading

def loop1 (in1):
    print('start loop 1 at:', time.ctime())
    print('我是参数：',in1)
    time.sleep(4)
    print('end loop 1 at:', time.ctime())

def loop2 (in1,in2):
    print('start loop 2 at:', time.ctime())
    print("我是参数",in1,"和参数",in2)
    time.sleep(2)
    print('end loop 2 at:', time.ctime())

def main():
    print('starting at:',time.ctime())
    t1= threading.Thread(target=loop1,args=("p1",))
    t1.start()
    #三个线程齐头并进，那个先输出都可能
    t2= threading.Thread(target=loop2,args=("p1","p2"))
    t2.start()
    print('all done at:',time.ctime())

if __name__ =='__main__':
    main()
    #一定要有while语言
    #因为启动多线程后本程序就作为主线程存在
    #如果主线程执行完毕，则子线程可能也需要终止
    while True:
        time.sleep(1)