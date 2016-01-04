from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "New Flaskito rulastonico running on a Java web container."

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='sample'):
    return render_template('hello.html', name=name)
    
@app.route('/hello2/')
@app.route('/hello2/<name>')
def hello2(name='sample2'):
    return render_template('hello2.html', name=name)

if __name__ == "__main__":
    app.run()
