from flask import Flask, request
from flask.views import MethodView
from flask import request
#from flask_json import json_response
from blueprint import APP
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(APP)
CORS(app)

#@app.route("/")
class hello(MethodView):
    def get(self):
#        dic = ''
#        if not dic:
#            return(json_response(dic,status_code=status.HTTP_404_NOT_FOUND))
        return "Hello, Returning from get"

    def post(self):
        
        print 'json:',request.get_json()
        print request.form['task']
        return "Hello, Returning from post"
        #return request.get_json()

    def put(self):
        return "Hello, Returning from put"

    def delete(self):
        return "Hello, Returning from put"

hl_view = hello.as_view('Hello')
app.add_url_rule('/Hello',view_func=hl_view, methods=['GET','POST','PUT','DELETE'])

class world(MethodView):
    def get(self):
        return "Hi, Return from get"

    def post(self):
        return "world, Return from post"

    def put(self):
        return "world, Return from PUT"

    def delete(self):
        return "world, Return from delete"

w_view = world.as_view('World')
app.add_url_rule('/World',view_func=w_view, methods=['GET','POST','PUT','DELETE'])

if __name__ == '__main__':
   print ("name1",__name__)
   app.run(host='0.0.0.0', debug=True)
