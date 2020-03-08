# 11.1 병행성
# 컴퓨터 Waiting
# - I/O 바운드
# - CPU 바운드
# 병행성
# - 동기(synchronous)   : 한 작업은 다른 작업을 따름.
# - 비동기(Asynchronous : 작업들이 독립적임.

# 11.1.2 프로세스

# dishes.py 참조

# 11.1.3 스레드
import threading

def do_this(what):
    whoami(what)

def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))

if __name__ == '__main__':
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("I'm function %s" % n,))
        p.start()


