import threading
import time
from flask import Flask
app = Flask(__name__)

def hello(name):
    print("hello %s"%name)

@app.route('/<path:path>')
def catch_all(path):
    t = threading.Timer(10.0, hello, [path])
    t.start()
    return "Done"

if __name__ == "__main__":
	app.run()
