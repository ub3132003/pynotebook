import os, time, random
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
        
def sayHello(say="hello"):
    print(time.time())
    time.sleep(5)
    print(say)
    print('Run child process %s '% os.getpid())
    return 1
      