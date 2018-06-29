import  threading
from time import sleep, ctime

loop = [4,2]

class ThreadFunc:
    def __init__(self,name):
        self.name = name

    def loop(self,nloop,nsec):
        #param nloop: loop函数的名称
        #param nsec: 系统休眠时间
        #return:
        print('start loop',nloop,'at',ctime())
        sleep(nsec)
        print('done loop',nloop,'at',ctime())

def main():
    print("starting at:",ctime())

    #ThreadFunc("loop").loop 跟以下两个式子相等
    #t = ThreadFunc("loop")
    #t.loop
    #以下t1和t2的定义方式相等
    t = ThreadFunc("loop")
    t1 = threading.Thread(target= t.loop,args=("loop1",4))
    t2 = threading.Thread(target=ThreadFunc('loop').loop,args=("loop2",2))
    #常见错误写法
    #t1 = threading.Thread(target=ThreadFunc('loop).loop(100,4))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("ALL done at:",ctime())

if __name__ == '__main__':
    main()