from flask import Flask, redirect, session, request, render_template
from form import FormFormulation
from loginCheck import loginCheck
from check import predictSomething


app = Flask(__name__)
app.secret_key="capstone"
global user;

@app.route("/")
def index():
  return  render_template('login.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
  user = loginCheck(request)
  if(user):
    session['id'] = user['id']
    session['major'] =  user['major']
    session['name'] = user['name']
    session['grade'] = user['grade']
    session['stattus'] = user['status']
    return redirect('/home')
  else:
    error_message = "학번 또는 비밀번호가 틀렸습니다."
    return render_template('login.html', error=error_message)

@app.route("/home")
def home():
  if(session):
    return render_template("home.html", user=session)
  else:
    error_message = "로그인이 필요한 페이지입니다."
    return render_template('login.html', error=error_message)

@app.route("/check")
def check():
  if(session):
    return render_template('check.html', user=session)
  else:
    error_message = "로그인이 필요한 페이지입니다."
    return render_template('login.html', error=error_message)

@app.route("/result", methods=['POST', 'GET'])
def result():
  if(session):
    student = FormFormulation(request);
    percent = predictSomething(student)
    if percent > 70:
      result = 1
    else:
      result = 0
    return render_template('prediction.html', user=session, percent=percent, result = result)
  else:
    error_message = "로그인이 필요한 페이지입니다."
    return render_template('login.html', error=error_message)

@app.route("/detail")
def detail():
  if(session):
    return render_template('detail.html', user=session)
  else:
    error_message = "로그인이 필요한 페이지입니다."
    return render_template('login.html', error=error_message)


if __name__=='__main__':
  app.run(debug= True)