from flask import Flask
app = Flask(__name__)

@app.route("/myflaskapp.py")

@app.route("/Google")
def google():
    helly = os.system('python hello.py')
    return helly

def get_x():
    x = 2
    return x
if __name__ == "__main__":

    app.run()
