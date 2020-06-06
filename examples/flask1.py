from flask import Flask, redirect, url_for, request, session
app = Flask(__name__)
app.secret_key = 'string'

"""
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
"""

@app.route('/')
def index():
    if 'username' in session:
         username = session['username']
         return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username/']
        return redirect(url_for('index'))
    
    return '''
	
    <form action = ""method = "post">
        <p><input type = text name = username/></p>
        <p><input type = submit value = Login/></p>
    </form>'''
	

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug = True)
