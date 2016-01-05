__author__ = 'avi & murali'
import struct
class forum_meta:
    def __init__(self):
      self.forum_name=None
def forum_meta_data(start,ind):
        li=[]
        i=0
        sum=start
        f=open("project1.dat","rb+")
        while i<33:
            sum=sum+(3*1024*1024)
            initial(sum)
            initial(sum+1048576)
            li.append(sum)
            i+=1
        length=len(li)
        i=0
        print li
        while i<length:
          ind=ind+20
          f.seek(ind)
          k=li[i]
          ad=struct.pack('i',k)
          f.write(ad)
          ind= f.tell()
          print ind
          i+=1
        f.close()

class meta:
    def __init__(self):
        self.count=0
def initial(n):
        f=open("project1.dat","rb+")
        ob=meta()
        f.seek(n,0)
        id=struct.pack('i',ob.count)
        f.write(id)
        f.seek(n,0)
        d= f.read(4)
        d,=struct.unpack('i',d)
        print d
        print f.tell()
        f.close()


def io_init():
    initial(1024)
    initial(10240)
    initial(17408)
    initial(24576)
    initial(31744)
    initial(38912)
    initial(46080)
    forum_meta_data(2150404,53252)
    forum_meta_data(109105156,108056580)
    forum_meta_data(217108484,216059908)
    forum_meta_data(325111812,324063236)
    forum_meta_data(433115140,432066564)
    forum_meta_data(541118468,540069892)


