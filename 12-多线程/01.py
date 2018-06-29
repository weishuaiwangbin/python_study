#利用time延时函数，生成两个函数
#利用多线程调用
#计算总运行时间
#练习带参数的多线程启动方法


import time
import _thread as thread

def  loop1():
    print('start loop 1 at:',time.ctime())
    time.sleep(4)
    print('end loop 1 at:',time.ctime())

def loop2():
    print('start loop 2 at:', time.ctime())
    time.sleep(2)
    print('end loop 2 at:', time.ctime())

def main():
    print('starting at:',time.ctime())
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    print('all done at:',time.ctime)

if __name__ =='__main__':
    main()
    while True:
        time.sleep(1)