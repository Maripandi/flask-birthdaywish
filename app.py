from flask import Flask,render_template,request
from datetime import date
app = Flask(__name__)


@app.route('/',methods = ['POST','GET'])
def home():
    datetoday = date.today()
    if request.method == 'POST':
        iname = request.form['name']
        idate = request.form['date']
        imessage = request.form['message']
        if idate == str(datetoday):
            name = 'Happy Birthday '+iname
            return render_template ('index.html',name = name, message = imessage,datetoday = datetoday)
    
    return render_template ('index.html',datetoday = datetoday)


if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        # port
        debug = True
        # options
    )
