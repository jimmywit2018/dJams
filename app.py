from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dJamsHome.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')

@app.route('/GoogleCalendar')
def GoogleCalendar():
    return render_template('GoogleCalendar.py')

@app.route('/search')
def search():
    return render_template('search.py')

@app.route('/CreatePlaylist')
def CreatePlaylist():
    return render_template('CreatePlaylist.py')

@app.route('/AddSongs')
def AddSongs():
    return render_template('AddSongs.py')

if __name__ == '__main__':
        app.run(debug=True)
