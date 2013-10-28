#import uwsgi
#from uwsgidecorators import spoolraw

from flask import Flask

#from flask.ext.pymongo import PyMongo

app = Flask(__name__)

#app.config['MONGO_HOST'] = 'localhost'
#app.config['MONGO_DBNAME'] = 'test'
#app.mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()