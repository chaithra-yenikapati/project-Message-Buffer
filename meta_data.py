__author__ = "avi & murali"
import struct
class meta:
    def __init__(self):
        self.count=0
    def start(self,n):
        f=open("project1.dat","rb+")
        f.seek(n,0)
        id=struct.pack('i',self.count)
        f.write(id)
        f.seek(n,0)
        d= f.read(4)
        print d
        print f.tell()
        f.close()

def start_meta():
    ob=meta()
    ob.start(1024)
    ob.start(10240)
    ob.start(17408)
    ob.start(24576)
    ob.start(31744)
    ob.start(38912)
    ob.start(46080)
    ob.start(5296132)#quest count
    ob.start(8441860)#
    ob.start(11587588)
    ob.start(14733316)
    ob.start(17879044)#ques count
    ob.start(5398533)#answer count