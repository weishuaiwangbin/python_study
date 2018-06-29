环境：
   - python3.6
   - pycharm
    
    https://www.cnblogs.com/jokerbj/p/7460260.html
    https://www.dabeaz.com/python/UnderstandingGIL.pdf


# 多线程 vs 多进程
- 程序：一堆代码以文本形式存入一个问答
- 进程：程序运行的一个状态
    - 包含地址空间，内存，数据栈等
    - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
- 线程：
    - 一个进程的独立运行片段，一个进程包含多个线程
    - 轻量化的进程
    - 共享互斥问题
    
- 全局解释器锁(GIL)
    - Python代码的执行是由python虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行
    
- Python包
    - thread：不太适用，python3改成_thread
    - threading：通行的包
    - 案例01：多线程，缩短总时间，使用_thread
    - 案例02：多线程，传参数

- threading的使用：
    - 直接利用threading.Thread生成Thread实例
        1. t = threading.Thread(target=xxx,args=(xxx,))
        2. t.start():启动多线程
        3. t.join():等待多线程执行完成
        4. 案例04
        5. 案例05：加入join
        - 守护线程-daemon
            - 如果在程序中将子线程设置成守护线程
            子线程或在主线程结束后自动退出
            - 一般任务，守护线程不重要或者不允许
            离开主线程独立运行
            - 守护线程案例能否有效果跟环境相关
            - 案例06 非守护线程
            - 案例07 守护线程
        - 线程常用属性  实例08
            - threading.currentThread：返回当前线程变量
            - threading.enumerate:返回一个保护正在运行的线程的list，正在运行的线程指的是线程启动后，结束前的所有线程
            - threading.activeCount:返回正在运行的线程数量，效果跟len(threading.enumerate)相同
            - threading.setName:给线程设置名字
            - threading.getName:得到线程的名字
    - 直接继承自threading.Thread
        - 直接继承Thread
        - 重写run方法
        - 类实例可以直接运行
        - 案例09
        
- 案例10  工业风案例