import urllib
import urllib2

class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def forum(username):

    try:
        while True:
            flag = 0
            index = 1
            counter = 0
            cat_list = ['1', '2', '3', '4', '5', '6']
            category = raw_input("1.General\n2.Education\n3.Politics"
                                 "\n4.Current Affairs\n5.Sports\n6.Technology\n\n7.logout\n"
                                 "select a category or LOGOUT:\n")
            if category == '7':
                print bcolors.OKBLUE + "\nBye Bye..!!\nWaiting to see you soon...:)" + bcolors.ENDC
                exit()
            elif category in cat_list:
                values = {'category':category} # eg: 1
                databytes = urllib.urlencode(values)
                req = urllib2.urlopen('http://localhost:8080/category', databytes) # sending to API
                forum_list = req.read() # list of forums
                if len(forum_list) == 0: # if no forums
                    print bcolors.WARNING + "\nSorry..!!\nNo forums posted yet...!!\n" \
                                            "You can create your own\n" + bcolors.ENDC
                    while True:
                        option = raw_input("Do you want to add a forum..??\n")
                        if option == 'yes':
                            flag = 1
                            counter = 1
                            break
                        elif option == 'no':
                            break
                        else:
                            print bcolors.FAIL + "Invalid choice\nEnter 'yes' or 'no'" + bcolors.ENDC
                else: # displaying list of forums
                    flag = 1
                    index = 1
                    print "\nAll the forums in the selected category are:"
                    forum_list = forum_list.split('|')
                    for each in range(len(forum_list),0,-1):
                        print index,' ',forum_list[each-1]
                        index += 1
                    print '\n'
                while flag == 1:
                    if counter == 1:
                        choice = '1'
                    else:
                        choice = raw_input("\nEnter your choice:\n1)Add Forum\n2)View a particular Forum\n\n" \
                                        "0)Back to categories\n")
                    if choice == '1':
                        forumName = raw_input("Enter the name of forum(20 characters max):\n")
                        count = 0
                        if len(forumName) == 0 or len(forumName) > 20:
                            print bcolors.FAIL + "Invalid forum name\n" + bcolors.ENDC
                            #forumName = raw_input("Enter the name of forum:\n")
                        else:
                            for each in forumName:
                                if each == ' ':
                                    count += 1
                            if count != len(forumName):
                                values = {'category':category,"forum":forumName,"username":username}
                                databytes = urllib.urlencode(values)
                                urllib2.urlopen('http://localhost:8080/addforum', databytes)
                                print bcolors.HEADER + "\nSuccess...!!\nForum created\n" + bcolors.ENDC
                                print "to add a question to a particular forum go into it.."
                                counter = 0
                            else:
                                print bcolors.FAIL + "Invalid forum name\n" + bcolors.ENDC
                    elif choice == '2':
                        flag1 = 0
                        counter1 = 0
                        index = 1
                        values = {'category':category} # eg: 1
                        databytes = urllib.urlencode(values)
                        req = urllib2.urlopen('http://localhost:8080/category', databytes) # sending to API
                        forum_list = req.read()
                        print "\nAll the forums in the selected category are:"
                        forum_list = forum_list.split('|')
                        for each in range(len(forum_list),0,-1):
                            print index, ' ', forum_list[each-1]
                            index += 1
                        print '\n'
                        forum_name = raw_input("Enter the FORUM ID to be viewed:\n")
                        if int(forum_name) < index:
                            forums = {'category':category, 'forumName':forum_list[int(forum_name)-1]}
                            databytes = urllib.urlencode(forums) # selecting a particular forum
                            req = urllib2.urlopen('http://localhost:8080/forum_questions', databytes)
                            questions = req.read() # list of all questions
                            if len(questions) == 0:  # if no questions present
                                print bcolors.WARNING + "\nSorry..!!\nNo questions posted yet...!!\n" \
                                                        "you can create your own" + bcolors.ENDC
                                while True:
                                    option = raw_input("\nDo you want to add a question..??\n")
                                    if option == 'yes':
                                        flag1 = 1
                                        counter1 = 1
                                        break
                                    elif option == 'no':
                                        break
                                    else:
                                        print bcolors.FAIL + "Invalid choice\nEnter 'yes' or 'no'" + bcolors.ENDC
                            else: # displaying all the questions
                                flag1 = 1
                                index = 1
                                print "\nAll the questions in the selected forum are:"
                                questions = questions.split('|')
                                for each in range(len(questions),0,-1):
                                    print index, ' ', questions[each-1]
                                    index += 1
                                print '\n'
                            while flag1 == 1:
                                if counter1 == 1:
                                    choice1 = '1'
                                else:
                                    choice1 = raw_input("Enter your choice\n1)Create question\n"
                                                "2)View a particular Question\n\n0)Back to forums\n")
                                if choice1 == '1':
                                    que_name = raw_input("Enter a question into the forum\n")
                                    if len(que_name) < 1024:
                                        values = {'category':category,"forum":forum_list[int(forum_name)-1],
                                                  'queName':que_name,"username":username}
                                        databytes = urllib.urlencode(values)
                                        req = urllib2.urlopen('http://localhost:8080/addque', databytes)
                                        print bcolors.HEADER + "\nSuccess...!!\nQuestion created" + bcolors.ENDC
                                        counter1 = 0
                                    else:
                                        print bcolors.FAIL + "question length exceded MAX limit\n" + bcolors.ENDC
                                elif choice1 == '2':
                                    flag2 = 0
                                    counter2 = 0
                                    forums = {'category':category, 'forumName':forum_list[int(forum_name)-1]}
                                    databytes = urllib.urlencode(forums) # selecting a particular forum
                                    req = urllib2.urlopen('http://localhost:8080/forum_questions', databytes)
                                    questions = req.read()
                                    index = 1
                                    print "\nAll the questions in the selected forum are:"
                                    questions = questions.split('|')
                                    for each in range(len(questions),0,-1):
                                        print index, ' ', questions[each-1]
                                        index += 1
                                    print '\n'
                                    que = raw_input("Enter a QUESTION ID to be searched:\n")
                                    if int(que) < index:
                                        que_dict = {'category':category,"forumName":forum_list[int(forum_name)-1],
                                                    "que":que}
                                        databytes = urllib.urlencode(que_dict)
                                        req = urllib2.urlopen('http://localhost:8080/que_answer', databytes)
                                        answers = req.read() # list of all answers
                                        if len(answers) == 0: # if no answers
                                            print bcolors.WARNING + "Sorry..!!\nNo one answered yet...!!\n" \
                                                                    "you can answer" + bcolors.ENDC
                                            while True:
                                                option = raw_input("\nDo you want to add an answer..??\n")
                                                if option == 'yes':
                                                    flag2 = 1
                                                    counter2 = 1
                                                    break
                                                elif option == 'no':
                                                    break
                                                else:
                                                    print bcolors.FAIL + "Invalid choice\nEnter 'yes' or 'no'" \
                                                                         "" + bcolors.ENDC
                                        else: # displaying answers
                                            flag2 = 1
                                            index = 1
                                            print "\nAll the answers in the selected question are:\n"
                                            answers = answers.split('|')
                                            for each in answers:
                                                print index, ' ', each
                                            print '\n'
                                        while flag2 == 1:
                                            if counter2 == 1:
                                                choice2 = '1'
                                            else:
                                                choice2 = raw_input("Enter your choice\n1)posting a new answer\n\n"
                                                                "0)Back to the list of Questions")
                                            if choice2 == '1':
                                                answer = raw_input("Enter an answer:\n")
                                                if len(answer) < 2048:
                                                    values = {'category':category,"forum":forum_list[int(forum_name)-1],
                                                              'queName':que,'answer':answer,"username":username}
                                                    databytes = urllib.urlencode(values)
                                                    req = urllib2.urlopen('http://localhost:8080/addans', databytes)
                                                    print bcolors.HEADER + "\nSuccess..!!\nAnswer added\n" \
                                                                           "" + bcolors.ENDC
                                                    print "to add an answer to a particular forum go into it.."
                                                    counter2 = 0
                                                else:
                                                    print bcolors.FAIL + "answer length exceeded the MAX " \
                                                                         "limit"+ bcolors.ENDC
                                            elif choice2 == '0':
                                                break
                                            else:
                                                print bcolors.FAIL + "Sorry..!!\nInvalid choice\nPlease " \
                                                                     "enter either 1 2 or 0\n" + bcolors.ENDC
                                    else:
                                        print bcolors.FAIL + "Sorry..!!\nInvalid choice\n"+ bcolors.ENDC
                                elif choice1 == '0':
                                    break
                                else:
                                    print bcolors.FAIL + "Sorry..!!\nInvalid choice\nPlease " \
                                                         "enter either 1 2 or 0\n" + bcolors.ENDC
                        else:
                            print bcolors.FAIL + "Sorry..!!\nInvalid choice\n"+ bcolors.ENDC
                    elif choice == '0':
                        break
                    else:
                        print bcolors.FAIL + "Sorry..!!\nInvalid choice\nPlease enter " \
                                             "either 1 2 or 0\n" + bcolors.ENDC
            else:
                print bcolors.FAIL + "Invalid category choice\nEnter a valid option" \
                                     " between 1 and 7" + bcolors.ENDC
    except urllib2.HTTPError:
        print bcolors.FAIL + "Sorry...!!\nname did not match..\nTry again\n\n" + bcolors.ENDC
        forum(username)

def login_again():

    print bcolors.OKGREEN+"Login to continue...:)\n"+ bcolors.ENDC
    username = raw_input("enter the username:")
    password = raw_input("enter password:")
    values = {'username':username,
              'password':password}
    databytes = urllib.urlencode(values)
    req = urllib2.urlopen('http://localhost:8080/register_user', databytes)
    while req.read() == 'not authenticated':
        print bcolors.FAIL + "sorry..!!\nusername or password not in records.."
        username = raw_input("re-enter the username:")
        password = raw_input("re-enter password:" + bcolors.ENDC)
        values = {'username':username,
              'password':password}
        databytes = urllib.urlencode(values)
        req = urllib2.urlopen('http://localhost:8080/register_user', databytes)
    print bcolors.OKBLUE + "authentication completed..\nproceed..!!\n" + bcolors.ENDC
    forum(username)

def login():

    print "Enter with\n'yes' for new user\n'no' for already existing user"
    user = raw_input("new user...??")
    if user == 'yes':
        username = raw_input("enter a user name:")
        values = {"username":username}
        databytes = urllib.urlencode(values)
        req = urllib2.urlopen('http://localhost:8080/username', databytes)
        store = req.read()
        while store == "invalid username" or store == 'exist':
            if req.read() == "invalid username":
                username = raw_input(bcolors.FAIL + "sorry..!!\nenter user name of length <= 10\n"
                                     "chars supported a-z, A-Z, 0-9:" + bcolors.ENDC)
                values = {"username":username}
                databytes = urllib.urlencode(values)
                req = urllib2.urlopen('http://localhost:8080/username', databytes)
            else:
                username = raw_input(bcolors.FAIL + "sorry..!!\nname already exists "
                                                   "try a different name:" + bcolors.ENDC)
                values = {"username":username}
                databytes = urllib.urlencode(values)
                req = urllib2.urlopen('http://localhost:8080/username', databytes)

        password = raw_input("enter a password:")
        values = {'password':password}
        databytes = urllib.urlencode(values)
        req = urllib2.urlopen('http://localhost:8080/password', databytes)
        while req.read() == "invalid password":
            password = raw_input(bcolors.FAIL + "password should be of length 6 to 10:" + bcolors.ENDC)
            values = {'password':password}
            databytes = urllib.urlencode(values)
            req = urllib2.urlopen('http://localhost:8080/password', databytes)

        re_enter = raw_input("re-enter the password:")
        values = {'password':password, 're_enter':re_enter}
        databytes = urllib.urlencode(values)
        req = urllib2.urlopen('http://localhost:8080/re_enter', databytes)
        while req.read() == "password mismatch":
            re_enter = raw_input(bcolors.FAIL + "password should be the same ad above\nre-"
                                                "enter:" + bcolors.ENDC)
            values = {'password':password, 're_enter':re_enter}
            databytes = urllib.urlencode(values)
            req = urllib2.urlopen('http://localhost:8080/re_enter', databytes)

        email = raw_input("enter an email:")
        values = {'email':email}
        databytes = urllib.urlencode(values)
        req = urllib2.urlopen('http://localhost:8080/email', databytes)
        while req.read() == "invalid email":
            email = raw_input(bcolors.FAIL + "enter a valid email of the form abc@xyz.com:" + bcolors.ENDC)
            values = {'email':email}
            databytes = urllib.urlencode(values)
            req = urllib2.urlopen('http://localhost:8080/email', databytes)

        user_info = {"username":username, "password":password, 'email':email}
        databytes = urllib.urlencode(user_info)
        req = urllib2.urlopen('http://localhost:8080/register', databytes)
        print bcolors.OKBLUE + "registration successful\nProceed...!!\n" + bcolors.ENDC
        login_again()
    elif user == 'no':
        login_again()
    else:
        print bcolors.FAIL + "try again..!!\nenter with\n'yes' for new user\n'no' for " \
                             "already existing user" + bcolors.ENDC
        login()

if __name__ == "__main__":
    login()