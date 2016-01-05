import struct
import time
from time import strftime
__author__ = 'avi & murali'
class ques_create:
    def __init__(self):
        self.question=None
        self.answer=None
        self.question_id=None
        self.q_time_stamp=None
        self.createdby=None

def question_create(ob,start):
        f=open("project1.dat","rb+")
        f.seek(start)
        k=f.read(4)
        n,=struct.unpack('i',k)
        count=n
        index=start+4+(n*1064)
        f.seek(index,0)
        f.seek(0,1)
        id=struct.pack('i',n)
        f.write(id)
        f.seek(0,1)
        id=struct.pack('1024s',ob.question)
        f.write(id)
        f.seek(0,1)
        time=struct.pack('16s',ob.q_time_stamp)
        f.write(time)
        f.seek(0,1)
        create=struct.pack('20s',ob.createdby)
        f.write(create)
        f.seek(start,0)
        count+=1
        k=struct.pack('i',count)
        f.write(k)
        print "created:"
def question_retrieve_list(start):
        f=open("project1.dat","rb+")
        f.seek(start)
        k=f.read(4)
        n,=struct.unpack('i',k)
        count=n
        i=0
        temp=[]
        li=[]
        while i<count:
           temp=[]
           index=start+4+(i*1064)
           f.seek(index,0)
           f.seek(0,1)
           n=f.read(4)
           id,=struct.unpack('i',n)
           temp.append(id)
           f.seek(0,1)
           #print f.tell()
           question=f.read(1024)
           que,=struct.unpack('1024s',question)
           temp.append(que)
           f.seek(0,1)
           time=f.read(16)
           time,=struct.unpack('16s',time)
           temp.append(time)
           f.seek(0,1)
           createdby=f.read(20)
           createdby,=struct.unpack('20s',createdby)
           temp.append(createdby)
           li.append(temp)
           i+=1
        return li

def answer_create(ob,start,id):
        temp=start
        temp+=102400
        f=open("project1.dat","rb+")
        f.seek(temp)
        k=f.read(4)
        k,=struct.unpack('i',k)
        count=k
        ind=(temp+4)+(k*2088)
        f.seek(ind,0)
        f.seek(0,1)
        id=struct.pack('i',id)
        f.write(id)
        f.seek(0,1)
        ans=struct.pack('2048s',ob.answer)
        f.write(ans)
        f.seek(0,1)
        time=struct.pack('16s',ob.q_time_stamp)
        f.write(time)
        f.seek(0,1)
        create=struct.pack('20s',ob.createdby)
        f.write(create)
        count+=1
        f.seek(temp)
        id=struct.pack('i',count)
        f.write(id)
        print "answered"
def retrieve_answers(id,start):
        temp=start
        li=[]
        res=[]
        temp+=102400
        f=open("project1.dat","rb+")
        f.seek(temp)
        k=f.read(4)
        k,=struct.unpack('i',k)
        count=k
        i=0
        while i<count:
            li=[]
            f.seek(0,1)
            index=f.read(4)
            index,=struct.unpack('i',index)
            if index==id:
               f.seek(0,1)
               ans=f.read(2048)
               ans,=struct.unpack('2048s',ans)
               li.append(ans)
               f.seek(0,1)
               time=f.read(16)
               time,=struct.unpack('16s',time)
               li.append(time)
               f.seek(0,1)
               created=f.read(20)
               created,=struct.unpack('20s',created)
               li.append(created)
               res.append(li)
            else:
                t=f.tell()
                t=t+2084
                f.seek(t,0)
            i+=1
        return res







def call_ques_create(ob):
      ob1=ques_create()
      ob=ques_create()
      ob.question="what is this"
      ob1.question_create(ob,5296133)


class category_creation_metadata:
    def __init__(self):
        self.category=None
        self.forum_name=None
        self.createdby=None
        self.timestamp=None

def cat_meta_data_write(ob):
        f=open("project1.dat","rb+")
        if ob.category=='general':
            f.seek(10240,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            ind=(10244+(n*68))
            f.seek(ind,0)
            fo=struct.pack("20s",ob.forum_name)
            f.write(fo+'|')
            creat=struct.pack("20s",ob.createdby)
            f.write(creat+'|')
            time=struct.pack("16s",ob.timestamp)
            f.write(time+"|")
            addr=struct.pack("i",53248)
            f.write(addr+"$")
            count=n
            n+=1
            f.seek(10240,0)
            id=struct.pack('i',n)
            f.write(id)
            return 53248,n
        elif ob.category=='education':
            f.seek(17408,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            ind=(17412+(n*68))
            f.seek(ind,0)
            fo=struct.pack("20s",ob.forum_name)
            f.write(fo+'|')
            creat=struct.pack("20s",ob.createdby)
            f.write(creat+'|')
            time=struct.pack("16s",ob.timestamp)
            f.write(time+"|")
            addr=struct.pack("i",108056576)
            f.write(addr+"$")
            count=n
            n+=1
            f.seek(17408,0)
            id=struct.pack('i',n)
            f.write(id)
            return 108056576,n
        elif ob.category=='politics':
            f.seek(24576,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            ind=(24580+(n*68))
            f.seek(ind,0)
            fo=struct.pack("20s",ob.forum_name)
            f.write(fo+'|')
            creat=struct.pack("20s",ob.createdby)
            f.write(creat+'|')
            time=struct.pack("16s",ob.timestamp)
            f.write(time+"|")
            addr=struct.pack("i",216059904)
            f.write(addr+"$")
            count=n
            n+=1
            f.seek(24576,0)
            id=struct.pack('i',n)
            f.write(id)
            return 216059904,n
        elif ob.category=='currentaffairs':
            f.seek(31744,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            ind=(31748+(n*68))
            f.seek(ind,0)
            fo=struct.pack("20s",ob.forum_name)
            f.write(fo+'|')
            creat=struct.pack("20s",ob.createdby)
            f.write(creat+'|')
            time=struct.pack("16s",ob.timestamp)
            f.write(time+"|")
            addr=struct.pack("i",324063232)
            f.write(addr+"$")
            count=n
            n+=1
            f.seek(31744,0)
            id=struct.pack('i',n)
            f.write(id)
            return 324063232,n
        elif ob.category=='sports':
            f.seek(38912,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            ind=(38916+(n*68))
            f.seek(ind,0)
            fo=struct.pack("20s",ob.forum_name)
            f.write(fo+'|')
            creat=struct.pack("20s",ob.createdby)
            f.write(creat+'|')
            time=struct.pack("16s",ob.timestamp)
            f.write(time+"|")
            addr=struct.pack("i",432066560)
            f.write(addr+"$")
            count=n
            n+=1
            f.seek(38912,0)
            id=struct.pack('i',n)
            f.write(id)
            return 432066560,n
        elif ob.category=='technology':
            f.seek(46080,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            ind=(46084+(n*68))
            f.seek(ind,0)
            fo=struct.pack("20s",ob.forum_name)
            f.write(fo+'|')
            creat=struct.pack("20s",ob.createdby)
            f.write(creat+'|')
            time=struct.pack("16s",ob.timestamp)
            f.write(time+"|")
            addr=struct.pack("i",540069888)
            f.write(addr+"$")
            count=n
            n+=1
            f.seek(46080,0)
            id=struct.pack('i',n)
            f.write(id)
            return 540069888,n

def cat_meta_data_retrieve(cat_name):
        f=open("project1.dat","rb+")
        if cat_name=='general':
            f.seek(10240,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            return 53248,n
        elif cat_name=='education':
            f.seek(17408,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            return 108056576,n
        elif cat_name=='politics':
            f.seek(24576,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            return 216059904,n
        elif cat_name=='currentaffairs':
            f.seek(31744,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            return 324063232,n
        elif cat_name=='sports':
            f.seek(38912,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            return 432066560,n
        elif cat_name=='technology':
            f.seek(46080,0)
            sz=struct.calcsize('i')
            n=f.read(sz)
            n,=struct.unpack('i',n)
            return 540069888,n
def pool_seek_add_forum(cat_pool,forum_count,forum_name):

    f=open("project1.dat","rb+")
    f.seek(cat_pool)
    meta_start=cat_pool+4
    meta_present=meta_start+(24*(forum_count-1))

    f.seek(meta_present)
    id=struct.pack("20s",forum_name)
    f.write(id)
    f.seek(0,1)
    n=f.read(4)
    forum_addr,=struct.unpack('i',n)
    return forum_addr


def pool_seek_read_forum(cat_pool,forum_count):
    f=open("project1.dat","rb+")
    f.seek(cat_pool)
    meta_start=cat_pool+4
    meta_present=meta_start+(24*forum_count)
    f.seek(meta_present)
    forum_name=f.read(20)
    id,=struct.unpack("20s",forum_name)
    f.seek(0,1)
    n=f.read(4)
    forum_addr,=struct.unpack('i',n)
    return  id,forum_addr

def insert_forum(ob):#forum insertion
    cat_pool,forum_count=cat_meta_data_write(ob)
    forum_name=ob.forum_name
    forum_addr=pool_seek_add_forum(cat_pool,forum_count,forum_name)
   # print "forum addr:",forum_addr

def retrieve_forum_list(cat_name):#forum retrieval
    addr,forum_count=cat_meta_data_retrieve(cat_name)
    li=[]
    i=0
    while i<forum_count:
      id=pool_seek_read_forum(addr,i)
      li.append(id)
      i+=1
    return  li
def retrieve_forum_addr(cat_pool,forum_count,forum_name):
    f=open("project1.dat","rb+")
    f.seek(cat_pool)
    meta_start=cat_pool+4
    i=0
    forum_name=struct.pack("20s",forum_name)
    while i<=forum_count:
        meta_present=meta_start+(24*i)
        f.seek(meta_present)
        id=f.read(20)
        id,=struct.unpack("20s",id)
        f.seek(0,1)
        n=f.read(4)
        addr,=struct.unpack('i',n)
        i+=1
        if id==forum_name:
            forum_addr=addr
            break
        else:
            continue
    return forum_addr


def post_question(f_obj,q_obj):#create question
    addr,n=cat_meta_data_retrieve(f_obj.category)
    f_addr=retrieve_forum_addr(addr,n,f_obj.forum_name)
    question_create(q_obj,f_addr)

def retrieve_question_list(f_obj):#retrieve questions list
    addr,n=cat_meta_data_retrieve(f_obj.category)
    f_addr=retrieve_forum_addr(addr,n,f_obj.forum_name)
    li=question_retrieve_list(f_addr)
    return li
def post_answers(f_obj,q_obj):#posting answers for a question
    addr,n=cat_meta_data_retrieve(f_obj.category)
    f_addr=retrieve_forum_addr(addr,n,f_obj.forum_name)
    answer_create(q_obj,f_addr,q_obj.question_id)

def retrieve_answers_list(f_obj,q_obj):#retrieve answers for a question
    addr,n=cat_meta_data_retrieve(f_obj.category)
    f_addr=retrieve_forum_addr(addr,n,f_obj.forum_name)
    li=retrieve_answers(q_obj.question_id,f_addr)
    return li
if __name__=="__main__":
    ob=category_creation_metadata()
    ob.category="general"
    ob.forum_name="china"
    ob.createdby="us"
    ob.timestamp='1234567890123456'
    #for i in range(20):
    #insert_forum(ob)
    q=ques_create()
    q.question="what is war between china and us "
    q.answer="for nuclear weapons"
    q.question_id=0
    q.q_time_stamp="1245678"
    q.createdby="avi"
    #li=retrieve_forum_list("education")
    #print li
    #print li
   # for i in range(10):
    #post_question(ob,q)
    #for i in range(10):
    #post_answers(ob,q)
    #li=retrieve_question_list(ob)
    #n=len(li)
    #for i in range(n):
     #  for j in range(4):
      #      print li[i][j]
    li=retrieve_answers_list(ob,q)
    n=len(li)
    for i in range(n):
        for j in range(3):
           print li[i][j]