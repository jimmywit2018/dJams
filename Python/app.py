from flask import Flask
app = Flask(__name__)

@app.route("/myflaskapp.py")

def get_x():
    x = 2
    return x
if __name__ == "__main__":

    app.run()
