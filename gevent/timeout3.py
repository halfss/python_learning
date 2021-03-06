import gevent
from gevent import Timeout

def wait():
    gevent.sleep(2)

timer = Timeout(1).start()
thread1 = gevent.spawn(wait)

try:
    thread1.join(timeout=timer)
except Timeout:
    print "Thread 1 time out"


timer = Timeout.start_new()
thread2 = gevent.spawn(wait)

try:
    thread2.get(timeout=timer)
except Timeout:
    print "Thread 2 timeout"


try:
    gevent.with_timeout(2, wait)
except Timeout:
    print" Thread 3 timeout" 
