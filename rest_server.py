__author__ = 'Ani'

import string

from bottle import route, run, request

from memory_cache import *


start_memory()

@route('/username', method='POST')
def username():
    data1 = request.POST['username']
    count = 0
    characters = string.letters + ' ' + string.digits
    if len(data1) <= 10:
        for each in data1:
            if each in characters:
                count += 1
                continue
            else:
                return 'invalid username'
    else:
        return "invalid username"
    if count == len(data1):
        result = username_availability(data1)
        if result == 'exist':
            return result

@route('/password', method='POST')
def password():
    data1 = request.POST['password']
    if len(data1) < 6 or len(data1) > 10:
        return "invalid password"

@route('/re_enter', method='POST')
def re_enter():
    data1 = request.POST['password']
    data2 = request.POST['re_enter']
    if data1 != data2:
        return "password mismatch"

@route('/email', method='POST')
def email():
    data1 = request.POST['email']
    dot = '.'
    atrate = '@'
    if dot not in data1:
        return "invalid email"
    elif atrate not in data1:
        return "invalid email"

@route('/register', method='POST')
def register_usr():
    data1 = request.POST['username']
    data2 = request.POST['password']
    data3 = request.POST['email']
    register(data1, data2, data3)

@route('/register_user', method='POST')
def authenticate_usr():
    data1 = request.POST['username']
    data2 = request.POST['password']
    result = authenticate(data1, data2)
    if result == "error in entry, please enter again":
        result = 'not authenticated'
        return result

# register email

category_list = {'1':'general', '2':'education',
                 '3':'politics', '4':'currentaffairs',
                 '5':'sports', '6':'technology'}
@route('/category', method='POST')
def category():
    data1 = request.POST['category']
    result_str = ''
    result = list_forums(category_list[data1])
    if result != []:
        for each in range(len(result)-1):
            result_str = result_str + result[each] + '|'
        result_str = result_str + result[-1]
    return result_str

@route('/forum_questions', method='POST')
def forum_ques():
    data1 = request.POST['category']
    data2 = request.POST['forumName']
    result = list_ques(category_list[data1], data2)
    result_str = ''
    if result != []:
        for each in range(len(result)-1):
            result_str = result_str + result[each] + '|'
        result_str = result_str + result[-1]
    return result_str

@route('/que_answer', method='POST')
def que_ans():
    data1 = request.POST['category']
    data2 = request.POST['forumName']
    data3 = request.POST['que']
    result = list_ans(category_list[data1], data2, data3)
    result_str = ''
    if result != []:
        for each in range(len(result)-1):
            result_str = result_str + result[each] + '|'
        result_str = result_str + result[-1]
    return result_str

@route('/addforum', method='POST')
def new_forum():
    data1 = request.POST['category']
    data2 = request.POST['forum']
    data3 = request.POST['username']
    add_forum(category_list[data1], data2, data3)

@route('/addque', method='POST')
def new_que():
    data1 = request.POST['category']
    data2 = request.POST['forum']
    data3 = request.POST['queName']
    data4 = request.POST['username']
    add_question(category_list[data1], data2, data3, data4)

@route('/addans', method='POST')
def new_ans():
    data1 = request.POST['category']
    data2 = request.POST['forum']
    data3 = request.POST['queName']
    data4 = request.POST['answer']
    data5 = request.POST['username']
    add_answer(category_list[data1], data2, data3, data4, data5)

run(host='localhost', port=8080, debug=True, reloader=True)