import re
from werkzeug.wrappers import response
from routes import student
from app import *


def test_emaillist():
    email_list=[]
    password_list=[]
    s2=student()
    print(s2.loginform('jhon14@gmail.com',"Jhon@123"))
    email_list.append(s2.email)
    password_list.append(s2.password)
    s3=student()
    print(s2.loginform("kalam@gmail.com","Kalam@123"))
    email_list.append(s2.email)
    password_list.append(s2.password)
    assert email_list == ['jhon14@gmail.com', 'kalam@gmail.com'] 
def test_loginfrom():
    response=app.test_client().get('/')
    assert response.status_code == 200
    assert b'Login Creditnals' in response.data
