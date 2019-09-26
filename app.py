from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>/<age>')
def hello_name(name,age):
   return 'Hello {} , Your age is {}'.format(name,age)


@app.route('/admin')
def index():
   return 'Hey User'

if __name__ == '__main__':
   app.run(debug = True)
