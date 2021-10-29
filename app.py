from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def loginform():
    return render_template('loginfrom.html')