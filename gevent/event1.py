import gevent
from gevent.event import Event

evt = Event()

def setter():
    print "A: hey wait for me, I have to do something"
    gevent.sleep(3)
    print "I am done"
    evt.set()

def waiter():
    print "I'll wait for you"
    evt.wait()
    print "It's about time"

def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
    ])

main()
