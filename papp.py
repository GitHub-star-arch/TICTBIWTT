from flask import Flask

object = Flask(__name__)

@object.route('/message')
def purpose():
    return('The meaning of Life is...')

if (__name__=='__main__'):
    object.run()