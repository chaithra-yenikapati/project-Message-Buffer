__author__ = 'chaithra'

from memory_cache import *
import threading
import socket
regist_lock=threading.Condition()
forum_lock=threading.Condition()
ques_lock=threading.Condition()
ans_lock=threading.Condition()
new_lock=threading.RLock()
old_lock=threading.RLock()
forums_flag=1
question_flag=1
ans_flag=1
def flushBuffer(conn):
    conn.recv(1)

def my_authenticate(username,password):
    message=authenticate(username,password)
    if message=="access granted":
        return True
    else:
        return False

def emailCheck(email):
    if '@' not in email or  '.com' not in email:
        return False
    if email[-4:]!='.com':
        return False
    if email.index('@')==0 or email.index('.')==0:
        return False
    elif email.index('@')-email.index('.')==-1:
        return False
    return True

def checkValidity(name,p1,p2,email):
    if len(name)>10:
        return "Username should be less than 10 characters"
    if len(p1)>10:
        return "Password should be less than 10 characters"
    if p1!=p2:
        return "Passwords do not match"
    if emailCheck(email)==False:
        return "Invalid email format"
    return True

def OldUser(conn):
    username=conn.recv(2048)
    password=conn.recv(2048)
    check=my_authenticate(username,password)
    if check==True:
        conn.sendall('True')
    else:
        conn.sendall("Authentication Failed")

    print password

def NewUser(conn):
    new_lock.acquire()
    username=conn.recv(2048)
    password=conn.recv(2048)
    pwd1=conn.recv(2048)
    print pwd1
    email=conn.recv(2048)
    flag=checkValidity(username,password,pwd1,email)
    if flag==True:
        register(username,password,email)
        conn.sendall("True")
    else:
        conn.sendall(flag)
    new_lock.release()

def listcategories(conn):
    list1=list_categories()
    conn.sendall("\n".join(list1))

def addforum(conn):
    global forums_flag
    print threading.current_thread().name,"forum Entered"
    category=conn.recv(2048)
    conn.sendall(category)
    print category,"acat "
    print threading.current_thread().name,"aafter cat"
    forumname=conn.recv(2048)
    print forumname,"aforum"
    conn.sendall(forumname)
    print threading.current_thread().name,"aafter forum"
    username=conn.recv(2048)
    print username
    print threading.current_thread().name,"aafter user"
    forum_lock.acquire()
    if forums_flag==0:
        print threading.current_thread().name,"awaiting"
        forum_lock.wait()
    forums_flag=0
    message=add_forum(category,forumname,username)
    conn.sendall(message)
    forum_lock.notifyAll()
    print threading.current_thread().name,"aanotified"
    forums_flag=1
    forum_lock.release()
    print threading.current_thread().name,"areleased"

def listforums(conn):
    category=conn.recv(2048)
    forumslist=list_forums(category)
    if len(forumslist)==0:
        conn.sendall('None')
    else:
        for i in range(0,len(forumslist)):
            conn.sendall(forumslist[i])
            flushBuffer(conn)
        conn.sendall('Over')


def postquestion(conn):
    global question_flag
    print threading.current_thread().name,"qEntered"
    category=conn.recv(2048)
    print category,"q cat"
    print threading.current_thread().name,"qEntered cat"
    conn.sendall(category)
    forumname=conn.recv(2048)
    print threading.current_thread().name,"qEntered forum"
    print forumname,"q forum"
    conn.sendall(forumname)
    question=conn.recv(2048)
    print question,"q ques"
    print threading.current_thread().name,"qEntered ques"
    conn.sendall(question)
    username=conn.recv(2048)
    print threading.current_thread().name,"Entered user"
    ques_lock.acquire()
    if question_flag==0:
        ques_lock.wait()
        print threading.current_thread().name,"qwaiting"
    question_flag=0
    message=add_question(category,forumname,question,username)
    conn.sendall(message)
    ques_lock.notifyAll()
    question_flag=1
    print threading.current_thread().name,"Entered notified"
    ques_lock.release()
    print threading.current_thread().name,"released"

def postanswer(conn):
    global ans_flag
    category=conn.recv(2048)
    print category,"ans cat"
    print threading.current_thread().name,"ans cat"
    conn.sendall(category)
    forumname=conn.recv(2048)
    print forumname,"ans forum"
    print threading.current_thread().name,"ans forum"
    conn.sendall(forumname)
    question=conn.recv(2048)
    print question,"ans ques"
    print threading.current_thread().name,"ans ques"
    conn.sendall(question)
    answer=conn.recv(2048)
    print answer,"ans ans"
    conn.sendall(answer)
    print threading.current_thread().name,"ans ans"
    username=conn.recv(2048)
    print threading.current_thread().name,"ans name"
    ans_lock.acquire()
    if ans_flag==0:
        ans_flag.wait()
        print threading.current_thread().name,"ans wait"
    ans_flag=0
    message=add_answer(category,forumname,int(question),answer,username)
    conn.sendall(message)
    ans_lock.notifyAll()
    print threading.current_thread().name,"notified"
    ans_flag=1
    ans_lock.release()
    print threading.current_thread().name,"released"


def getquestion(conn):
    category=conn.recv(2048)
    conn.sendall(category)
    forumname=conn.recv(2048)
    qstnslsit=list_ques(category,forumname)
    print qstnslsit
    if len(qstnslsit)==0:
        conn.sendall('None')
    else:
        for i in range(0,len(qstnslsit)):
            conn.sendall(qstnslsit[i])
            flushBuffer(conn)
        conn.sendall('Over')

def getanswer(conn):
    category=conn.recv(2048)
    conn.sendall(category)
    forumname=conn.recv(2048)
    conn.sendall(forumname)
    question=conn.recv(2048)
    anslist=list_ans(category,forumname,question)
    if len(anslist)==0:
        conn.sendall('None')
    else:
        for i in range(0,len(anslist)):
            conn.sendall(anslist[i])
            flushBuffer(conn)
        conn.sendall('Over')

def options(conn):
    while True:
            data=conn.recv(2048)
            print data
            if data=='1':
               listcategories(conn)
            elif data=='2':
                addforum(conn)
            elif data=='3':
                listforums(conn)
            elif data=='4':
                postquestion(conn)
            elif data=='5':
                postanswer(conn)
            elif data=='6':
                getquestion(conn)
            elif data=='7':
                getanswer(conn)
            elif data=='8':
                NewUser(conn)
            elif data=='9':
                OldUser(conn)
            else:
                return None


def createSocket():
    host=socket.gethostname()
    port=12513
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(8)
    while True:
        conn,addr=s.accept()
        print "connected to:",addr
        th=threading.Thread(None,options,args=(conn,))
        th.start()


if __name__=="__main__":
    start_memory()
    createSocket()