__author__ = 'chaithra & surya'


from class_formats import *
from category_meta_data import *
from user_info import *
import time
from time import strftime

class user1:
    def __init__(self,username='',password='',email=''):
        self.userid=username
        self.password=password
        self.email=email

class category_node:
    def __init__(self,cat_name=None):
        self.cat_name=cat_name
        self.next_cat=None
        self.forum_link=None

class forum_node:
    def __init__(self,forum_name=None):
        self.forum_name=forum_name
        self.next_forum=None
        self.ques_link=None

class ques_node:
    def __init__(self,ques=None,ques_id=None):
        self.ques=ques
        self.ques_id=ques_id
        self.next_ques=None
        self.ans_link=None

class ans_node:
    def __init__(self,ans=None):
        self.ans=ans
        self.next_ans=None
def trim(str):
    s=''
    i=0
    try:
        while str[i]!='\x00':
            s+=str[i]
            i+=1
    except:
        return s
    return s
def trim1(str):
    s=''
    i=0
    count=0
    while True:
            if str[i]=='\x00':
                if count==0:
                    count=1
                    s+=str[i]
                    i+=1
                    continue
                else:
                    break
            else:
                count=0
                s+=str[i]
            i+=1
    return s
username_list=[]
password_list=[]
email_list=[]
head=category_node('sports')
temp_head=head
temp_head.next_cat=category_node('general')
temp_head=temp_head.next_cat
temp_head.next_cat=category_node('education')
temp_head=temp_head.next_cat
temp_head.next_cat=category_node('currentaffairs')
temp_head=temp_head.next_cat
temp_head.next_cat=category_node('politics')
temp_head=temp_head.next_cat
temp_head.next_cat=category_node('technology')
user_obj_list=get_user_table()
for user in user_obj_list:
        username_list=username_list+[trim(user.userid)]
        password_list=password_list+[trim(user.password)]
        email_list=email_list+[trim(user.email)]


def add_forum_to_list(category_name,forum_name):
    temp_head=head
    while temp_head.cat_name!=category_name:
        temp_head=temp_head.next_cat
    new_forum=forum_node(forum_name)
    new_forum.next_forum=temp_head.forum_link
    temp_head.forum_link=new_forum

def add_question_to_list(category_name,forum_name,ques):
    temp_head=head
    while temp_head.cat_name!=category_name:
        temp_head=temp_head.next_cat
    temp_head=temp_head.forum_link
    if temp_head!=None:
        while temp_head.next_forum and temp_head.forum_name!=forum_name:
            temp_head=temp_head.next_forum
    new_ques=ques_node(ques)
    new_ques.next_ques=temp_head.ques_link
    if new_ques.next_ques:
        new_ques.ques_id=new_ques.next_ques.ques_id+1
    else:
        new_ques.ques_id=0
    temp_head.ques_link=new_ques


def add_answer_to_list(category_name,forum_name,ques,ans):
    temp_head=head
    ques=int(ques)-1
    while temp_head.cat_name!=category_name:
        temp_head=temp_head.next_cat
    temp_head=temp_head.forum_link
    while temp_head.forum_name!=forum_name and temp_head.next_forum!=None:
        temp_head=temp_head.next_forum
    temp_head=temp_head.ques_link
    if temp_head!=None:
        while temp_head.ques_id!=ques and temp_head.next_ques!=None:
            temp_head=temp_head.next_ques
    new_ans=ans_node(ans)
    new_ans.next_ans=temp_head.ans_link
    temp_head.ans_link=new_ans

def get_forums(category_name):
    #print category_name
    forum_list=retrieve_forum_list(category_name)
    #print forum_list
    for i in range(len(forum_list)):
        forum_list[i]=trim(forum_list[i][0])
    return forum_list

def get_questions(categoy_name,forum_name):
    f=forum()
    f.category=categoy_name
    f.forum_name=forum_name
    qlist = retrieve_question_list(f)
    for i in range(len(qlist)):
        qlist[i][1]=trim(qlist[i][1])
    return qlist


def get_answers(category_name,forum_name,ques_id):
    f=forum()
    f.category=category_name
    f.forum_name=forum_name
    q=ques_create()
    q.question_id=ques_id
    anslist = retrieve_answers_list(f,q)
    #print anslist
    for i in range(len(anslist)):
        anslist[i][0] = trim(anslist[i][0])
    return anslist
def authenticate(user_name,password):
    if user_name in username_list and password in password_list:
        return "access granted"
    else:
        return "error in entry, please enter again"

def username_availability(user_name):
    if user_name in username_list:
        return "exist"
    else:
        return "available"

def email_availability(email):
    if email in email_list:
        return "exist"
    else:
        return "available"


def register(userid,password,email):
    new_user=user_info()
    new_user.userid=userid
    new_user.password=password
    new_user.email=email
    make_new_user(new_user)
    username_list.append(userid)
    password_list.append(password)
    email_list.append(email)


def add_forum(category_name,forum_name,user):
    add_forum_to_list(category_name,forum_name)
    send_forum=forum()
    send_forum.forum_name=forum_name
    send_forum.category=category_name
    send_forum.createdby=user
    send_forum.timestamp=strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    insert_forum(send_forum)
    return "Forum created"

def add_question(category_name,forum_name,ques,user):
    add_question_to_list(category_name,forum_name,ques)
    f_obj=forum()
    f_obj.category=category_name
    f_obj.forum_name=forum_name
    q_obj=ques_create()
    q_obj.question=ques
    q_obj.q_time_stamp=strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    q_obj.createdby=user
    post_question(f_obj,q_obj)
    return "Question added successfully"

def add_answer(category_name,forum_name,ques,ans,user):
    add_answer_to_list(category_name,forum_name,ques,ans)
    f_obj=forum()
    f_obj.category=category_name
    f_obj.forum_name=forum_name
    q_obj=ques_create()
    q_obj.question_id=int(ques)-1
    q_obj.answer=ans
    q_obj.q_time_stamp=strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    q_obj.createdby=user
    post_answers(f_obj,q_obj)
    return "Answer added successfully"

def list_forums(category_name):
    temp_head=head
    while temp_head.next_cat and temp_head.cat_name!=category_name:
        temp_head=temp_head.next_cat
    temp_head=temp_head.forum_link
    forums=[]
    while temp_head:
        forums.append(temp_head.forum_name)
        temp_head=temp_head.next_forum
    return forums

def list_ques(category_name,forum_name):
    temp_head=head
    while temp_head.next_cat and temp_head.cat_name!=category_name:
        temp_head=temp_head.next_cat
    forum_head=temp_head.forum_link
    while forum_head.next_forum and forum_head.forum_name!=forum_name:
        forum_head=forum_head.next_forum
    ques=[]
    if forum_head.forum_name==forum_name:
        ques_head=forum_head.ques_link
        while ques_head:
            ques.append(ques_head.ques)
            ques_head=ques_head.next_ques
    return ques

def list_ans(category_name,forum_name,ques):
    temp_head=head
    ques=int(ques)-1
    while temp_head.next_cat and temp_head.cat_name!=category_name:
        temp_head=temp_head.next_cat
    temp_head=temp_head.forum_link
    while temp_head.next_forum and temp_head.forum_name!=forum_name:
        temp_head=temp_head.next_forum
    temp_head=temp_head.ques_link
    while temp_head.next_ques and temp_head.ques_id!=ques:
        temp_head=temp_head.next_ques
    ans=[]
    if temp_head.ques_id==ques:
        temp_head=temp_head.ans_link
        while temp_head:
            ans.append(temp_head.ans)
            temp_head=temp_head.next_ans
    return ans

def list_categories():
    temp_head=head
    categories=[]
    while temp_head:
        categories=categories+[temp_head.cat_name]
        temp_head=temp_head.next_cat
    return categories

def start_memory():
    cat_list=list_categories()
    #print cat_list
    for cat in cat_list:
      cat_head=head
      while cat_head.cat_name!=cat:
        cat_head=cat_head.next_cat
      #print "get forums"
      forum_list=get_forums(cat)
      if forum_list:
        for each_forum in forum_list:
            new_forum=forum_node(each_forum)
            new_forum.next_forum=cat_head.forum_link
            cat_head.forum_link=new_forum
            forum_head=cat_head.forum_link
            ques_list=get_questions(cat,each_forum)
            for each_ques in ques_list:
                new_ques=ques_node(each_ques[1],each_ques[0])
                new_ques.next_ques=forum_head.ques_link
                forum_head.ques_link=new_ques
                ques_head=forum_head.ques_link
                ans_list=get_answers(cat,each_forum,each_ques[0])
                for each_ans in ans_list:
                    new_ans=ans_node(each_ans[0])
                    new_ans.next_ans=ques_head.ans_link
                    ques_head.ans_link=new_ans

def generate_test_input():
    category_list=list_categories()
    for each_cat in category_list:
        for i in range(0,20):
            add_forum(each_cat,"forum"+str(i),"chaithra")
            for j in range(0,20):
                add_question(each_cat,"forum"+str(i),"question"+str(j),"chaithra")
                for k in range(0,10):
                    add_answer(each_cat,"forum"+str(i),j,"answer"+str(j),"chaithra")


if __name__=='__main__':
    start_memory()
    #print list_ans("education",'forum0',1)
    #print username_list,password_list
    #register('surya','suri','sury@sdjg.com')
    #print username_list
    #add_forum('currentaffai','gk','chaitu')
    #add_forum('politics','trs','chaitu')
    #add_forum('education','engineering','chaitu')
    #print list_forums('sports')
    #add_question('politics','congress','where is priyanka gandhi','jump')
    #add_question('education','engg','dislike?','chaitu')
    #add_answer('sports','polo',0,'yes hello','chaitu')
    #add_answer('education','engg',2,'no','chaitu')
    #print list_ques('sports','polo')
    #print get_forums('currentaffairs')
    print get_questions('sports','forum0')
    #print get_answers('general','peace',2)
    #print list_categories()
    #print list_forums('politics')
    #print list_ques('politics','congress')
    #print list_ques('sports','forum0')
    #print get_answers('general','china',0)
    #print list_ans('general','china','2')
    #print get_user_table()
    #print username_list
    #print password_list
    #print email_list
    #add_forum('currentaffairs','countries','chaitu')
