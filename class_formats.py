__author__ = ''
#class formats to be supported by IO group
#please follow this as we need to implement as meta data and store into the file

class user:
    def __init__(self,username='',password='',email=''):
        self.userid=username
        self.password=password
        self.email=email

class category:
    def __init__(self,categoryname='',forums=[]):
        self.category_name=categoryname
        self.forums=forums

class forum:
    def __init__(self):
        self.category=None
        self.forum_name=None
        self.createdby=None
        self.timestamp=None

class ques_create:
    def __init__(self):
        self.question=None
        self.answer=None
        self.question_id=None
        self.q_time_stamp=None
        self.createdby=None
class answers:
    def __init__(self,answers=[],created_by=[],timestamp=[]):
        self.answers=answers
        self.created_by=created_by
        self.timestamp=timestamp
