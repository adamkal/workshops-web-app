from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')


@app.route('/dupa')
def dupa(): 
    return 'dupa'


@app.route('/twoja/<var>/')
def twoja(var):
    if var == 'ssij':
        return render_template('home2.html', name=var)
    return render_template('home.html', name=var)


@app.route('/user/<int:user_id>/')
def show_user(user_id):
    return f"User with id: {user_id}"


@app.route('/formularz', methods=['POST', 'GET'])
def formularz():
    
    ziom = None
    xxxx = None
    if request.method == 'POST':
        ziom = request.form.get('imie')
        xxxx = request.form.get('xxxx')

        print(dict(request.form))    
    return render_template('form.html', ksywa=ziom, xxxx=xxxx)
