import os
import sys
import subprocess
from flask import Flask
app = Flask(__name__)

@app.route("/CreatePlaylist")
def CreatePlaylist():
    os.system('python CreatePlaylist.py')

@app.route("/search")
def search():
    os.system('python search.py')

@app.route("/hello")
def hello():
    hello = subprocess.check_output([sys.executable, "hello.py"])
    return(str(hello))

def get_x():
    x = 2
    return x
if __name__ == "__main__":
    app.run()
