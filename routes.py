from flask import Flask, render_template,request

class student:
    email_list=[]
    password_list=[]
    def loginform(self,email,password):
    
        self.email=email
        self.password=password
        
