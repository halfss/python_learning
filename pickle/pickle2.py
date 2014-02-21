#codint=utf8

import Cpickle as pickle
import random
import os

import time

def main():
    d = {}
    a = []
    for i in range(LENGTH):
        a.append(random.randint(0, 255))
    
    d["a"] = a

    print "dumping..."
    
    t1 = time.time()
    pickle.dump(d, open("tmp1,dat", "wb"), True)
    print "dump1: %.3fs" % (time.time() - t1)
    
    t1 = time.time()
    pickle.dump(d, open("tmp2.dat", "w"))
    print "dump2: %.3fs" % (time.time() - t1)

    s1 = os.stat("tmp1.dat").st_size
    s2 = os.stat("tmp2.dat").st_size

    print "%d, %d, %.2fs%%" % (s1, s2, 100 * s1/s2)

    print "loading..."

    t1 = time.time()
    obj1 = pickle.load(open("tmp1.dat", 'rb'))
    print "load1: %.3fs" % (time.time() - t1)


    t1 = time.time()
    obj2 = pickle.load(open("tmp2.dat", 'rb'))
    print "load1: %.3fs" % (time.time() - t1)

if __name__ == "__main__":
    main()
    
    
