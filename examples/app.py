from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('text.txt')

@app.route('/hello/<name>')
def hello(name):
    return render_template('text.html',name=name)

#@app.route('/admin')
#def hellodmin():
#    return 'hello_admin'

#@app.route('/guest/<guest>')
#def hello_guest(guest):
#    return 'hello %s as guest' % guest

#@app.route('/hello/<name>')
#def hello_user(name):
#    if name == 'admin':
#        return redirect(url_for('hello_admin'))
#    else:
#        return redirect(url_for('hello_guest', guest = name))

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0')
