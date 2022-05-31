from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return  render_template('index.html')

@app.route("/check")
def check():
  return render_template('check.html')

@app.route("/result", methods=['POST', 'GET'])
def result():
  if request.method == 'POST':
    print("Active!!")
    print(f"This is form data: {request.form}")
    score = float(request.form['score'])
    if(request.form['subject'] == "opic"):
      if(request.form['opic'] == "AL"):
        toeic_opic = float(4)
      elif(request.form['opic'] == "IH"):
        toeic_opic = float(3)
      elif(request.form['opic'] == "IM1" or request.form['opic'] == "IM2" or request.form['opic'] == "IM3"):
        toeic_opic = float(2)
      else:
        toeic_opic = float(1)
    elif(request.form['subject'] == "toeic" or request.form['toeic'] == "LV7"):
        if(request.form['toeic'] == "LV8"):
          toeic_opic = float(4)
        elif(request.form['toeic'] == "LV6"):
          toeic_opic = float(3)
        else:
          toeic_opic = float(2)
    activity = float(request.form['activity'])
    volunteer = float(request.form['volunteer'])
    inter = float(request.form['intern'])
    print(score, toeic_opic, activity, volunteer, inter)
    return render_template('index.html')

if __name__=='__main__':
  app.run(debug= True)