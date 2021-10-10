from flask import Flask

lab4 = Flask(__name__)


@lab4.route('/api/v1/hello-world-15')
def hello_world():
    return 'Hello World 15'
