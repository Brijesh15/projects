from flask import Blueprint ,Flask

APP = Blueprint('APP',__name__)

@APP.route('/blue',methods=['GET'])
def blue1():
    return 'Returning from Blueprint!!'
