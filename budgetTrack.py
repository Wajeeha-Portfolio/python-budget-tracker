from flask import Flask
app = Flask(__name__)

import upload_handler
app.register_blueprint(upload_handler.upload_handler)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()