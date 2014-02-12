import socket
print (socket.socket)

print "after monkey patch"
from gevent import monkey
monkey.patch_socket()
print socket.socket
