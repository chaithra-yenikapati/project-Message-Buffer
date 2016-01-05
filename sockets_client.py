

import socket
import os
import getpass

cat_list = ['1.sports','2.general','3.education','4.currentaffairs','5.politics','6.technology','7.Logout']

def flushBuffer(s):
    s.sendall('\0')

def myprint():
    print "CATEGORIES"
    for i in range(0,len(cat_list)):
        print cat_list[i]
    print "\n\n"

def NewUser(s):
    s.sendall('8')
    username=raw_input("Enter the user name :")
    s.sendall(username)
    s.sendall(getpass.getpass("Enter the password: "))
    s.sendall(getpass.getpass("Re Enter the password :"))
    s.sendall(raw_input("Enter email id :"))
    data=s.recv(2048)
    if data=='True':
        print "Registration Successful\n"
        os.system('cls')
        OldUser(s)
    else:
        print data
        NewUser(s)

def OldUser(s):
    s.sendall('9')
    name=raw_input("Enter the user name:")
    s.sendall(name)
    s.sendall(getpass.getpass("Enter the password:"))
    data=s.recv(2048)
    #print data
    if data=='True':
        os.system('cls')
        print "Welcome ",name,"\n"
        return name
    else:
        print data
        OldUser(s)

def addForum(s,category,username):
    s.sendall('2')
    s.sendall(category)
    s.recv(2048)
    forumname=raw_input("Enter forum name :")
    while True:
        if len(forumname)>20:
            print "Forum name should be less than 10 characters"
            forumname=raw_input("Enter forum name :")
        else:
            break
    s.sendall(forumname)
    s.recv(2048)
    os.system('cls')
    s.sendall(username)
    print s.recv(2048)


def postQuestion(s,category,forumname,username):
    s.sendall('4')
    s.sendall(category)
    s.recv(2048)
    s.sendall(forumname)
    s.recv(2048)
    question=raw_input("Enter your question :")
    while True:
        if len(question)>1024:
            print "Question length exceeded maximum size"
            question=raw_input("Enter your question :")
        else:
            break
    os.system('cls')
    s.sendall(question)
    s.recv(2048)
    s.sendall(username)
    print s.recv(2048)
    return question
def postAnswer(s,category,forumname,question,username):
    s.sendall('5')
    s.sendall(category)
    s.recv(2048)
    s.sendall(forumname)
    s.recv(2048)
    s.sendall(question)
    s.recv(2048)
    answer=raw_input("Enter your answer :")
    while True:
        if len(answer)>2048:
            print "Answer length exceeded maximum size"
            answer=raw_input("Enter your answer :")
        else:
            break
    s.sendall(answer)
    os.system('cls')
    s.recv(2048)
    s.sendall(username)
    print s.recv(2048)

def screen3(s,category,forumname,question,username,ques_list):
    #print "The selected question is: ",ques_list[len(ques_list)-int(question)]
    while 1:
        print "Question: ",ques_list[len(ques_list)-int(question)]
        print "Select an option :\n\n"
        ch=raw_input('1.View Answers\n2.Post Answer\n3.Go Back\n')
        os.system('cls')
        if ch=='1':
            ans_list=[]
            s.sendall('7')
            s.sendall(category)
            s.recv(2048)
            s.sendall(forumname)
            s.recv(2048)
            s.sendall(question)
            data=s.recv(2048)
            if data!='None':
                while 1:
                    if data!="Over":
                        ans_list.append(data)
                        flushBuffer(s)
                    else:
                        break
                    data=s.recv(2048)
            if data=='None':
                print "Question: ",ques_list[len(ques_list)-int(question)]
                print "No answers posted....Do you want to post an answer?"
                ch1=raw_input('1.Yes\n2.No\n')
                os.system('cls')
                if ch1=='1':
                    postAnswer(s,category,forumname,question,username)
                elif ch=='2':
                    return
            else:
                print "Question: ",ques_list[len(ques_list)-int(question)]
                print "ANSWERS LIST :\n\n"
                size=len(ans_list)
                for i in range(size-1,-1,-1):
                    print size-i,".",ans_list[i]
                print "\n\n\n\n"
        elif ch=='2':
            print "Question: ",ques_list[len(ques_list)-int(question)]
            postAnswer(s,category,forumname,question,username)
        elif ch=='3':
            return


def screen2(s,category,forumname,username):
    print "You are in ",forumname,"forum\n"
    while 1:
        print "Select an option :\n\n"
        ch=raw_input('1.View Questions\n2.Post Question\n3.Select Question\n4.Go Back\n')
        if ch=='1':
            os.system('cls')
            ques_list=[]
            s.sendall('6')
            s.sendall(category)
            s.recv(2048)
            s.sendall(forumname)
            data=s.recv(2048)
            if data!='None':
                while 1:
                    if data!="Over":
                        ques_list.append(data)
                        flushBuffer(s)
                    else:
                        break
                    data=s.recv(2048)
            if data=='None':
                print "No Questions posted....Do u want to post a question?"
                ch1=raw_input('1.Yes\n2.No\n')
                os.system('cls')
                if ch1=='1':
                    ques_list.append(postQuestion(s,category,forumname,username))
                elif ch1=='2':
                    return
            else:
                print "You are in",forumname,"forum\n"
                print "QUESTIONS LIST :\n\n"
                size=len(ques_list)
                for i in range(size-1,-1,-1):
                    print size-i,".",ques_list[i]
                print "\n\n\n\n"
        elif ch=='2':
            os.system('cls')
            postQuestion(s,category,forumname,username)
        elif ch=='3':
            os.system('cls')
            ques_list=[]
            s.sendall('6')
            s.sendall(category)
            s.recv(2048)
            s.sendall(forumname)
            data=s.recv(2048)
            if data!='None':
                while 1:
                    if data!="Over":
                        ques_list.append(data)
                        flushBuffer(s)
                    else:
                        break
                    data=s.recv(2048)
            if data=='None':
                print "No Questions posted....Do u want to post a question?"
                ch1=raw_input('1.Yes\n2.No\n')
                os.system('cls')
                if ch1=='1':
                    ques_list.append(postQuestion(s,category,forumname,username))
                elif ch1=='2':
                    return
            else:
                print ""
                print "QUESTIONS LIST :\n\n"
                size=len(ques_list)
                for i in range(size-1,-1,-1):
                    print size-i,".",ques_list[i]
                print "\n\n\n\n"
            question=raw_input('Select the question number\n')
            os.system('cls')
            screen3(s,category,forumname,question,username,ques_list)
            print "QUESTIONS LIST :\n\n"
            size=len(ques_list)
            for i in range(size-1,-1,-1):
                print size-i,".",ques_list[i]
            print "\n\n\n\n"
        elif ch=='4':
            os.system('cls')
            return

def screen1(s,category,username):
    print "You are in ",category,"category\n"
    while 1:
        forums_list=[]
        s.sendall('3')
        s.sendall(category)
        data=s.recv(2048)
        if data!='None':
                while 1:
                    if data!="Over":
                        forums_list.append(data)
                        flushBuffer(s)
                    else:
                        break
                    data=s.recv(2048)
        if data=='None':
            print "No Forums created....Do u want to add a new Forum?"
            ch=raw_input('1.Yes\n2.No\n')
            os.system('cls')
            if ch=='1':
                addForum(s,category,username)
            else:
                return 2
        else:
            print "FORUMS LIST :\n"
            for i in range(0,len(forums_list)):
                print forums_list[i]
            print "\n\n\n\n"
            print "Enter your choice"
            ch=raw_input('1.Add Forum\n2.View Forum\n3.Go Back\n')
            if ch=='1':
                os.system('cls')
                addForum(s,category,username)
            elif ch=='2':
                forumname = raw_input("Enter forumname :")
                while True:
                    if forumname not in forums_list:
                        print "Enter valid forum name"
                        forumname=raw_input("Enter forumname :")
                    else:
                        break
                os.system('cls')
                screen2(s,category,forumname,username)
            elif ch=='3':
                os.system('cls')
                return

def main(s,username):
    while 1:
        myprint()
        choice=raw_input("Select the category :")
        os.system('cls')
        if choice=='7':
            return
        category=cat_list[int(choice)-1][2:]
        screen1(s,category,username)

def createsocket():
    port=12513
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.connect((host , port))
    print "Welcome to Forum-11"
    choice=raw_input("1.SignIn\n2.SignUp\n")
    os.system('cls')
    if choice=='1':
        username=OldUser(s)
    else:
        username=NewUser(s)
    main(s,username)

if __name__ == "__main__":
    try:
        os.system('cls')
        os.system("color F0")
        createsocket()
    except Exception:
        print Exception
    finally:
        os.system("color 0F")