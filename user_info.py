__author__ ='avi & murali'
import struct
class user_info:
    def __init__(self):
        self.password = None
        self.userid = None
        self.email = None
    def display(self):
        print "user id:",self.userid
        print "password:",self.password
        print "email:",self.email

def insert_user(ob):#add user
      f = open("project1.dat", "rb+")
      f.seek(1024,0)
      sz=struct.calcsize('i')
      n=f.read(sz)
      n,=struct.unpack('i',n)
      ind=(1028 + (n * 40))
      f.seek(ind,0)
      id = struct.pack('10s', ob.userid)
      f.write(id)
      ps = struct.pack('10s',ob.password)
      f.write(ps)
      em=struct.pack('20s', ob.email)
      f.write(em)
      n+=1
      f.seek(1024,0)
      id=struct.pack('i',n)
      f.write(id)
      f.close()
def retrieve_user(n):
        ob=user_info()
        f = open("project1.dat", "rb+")
        ind=(1028 + (n * 40))
        f.seek(ind,0)
        us=f.read(10)
        ps=f.read(10)
        em=f.read(20)
        ob.email=em
        ob.userid=us
        ob.password=ps
        print "count=",n
        f.close()
        return ob

def make_new_user(ob1):
     insert_user(ob1)
def get_user_table():#user id retrieval table func
    r=user_info()
    li=[]
    f = open("project1.dat", "rb+")
    f.seek(1024,0)
    sz=struct.calcsize('i')
    n=f.read(sz)
    n,=struct.unpack('i',n)
    f.close()
    i=0
    while i<n:
        r=retrieve_user(i)
        li.append(r)
        i+=1
    f.close()
    return li
