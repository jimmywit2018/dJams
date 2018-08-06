import sqlite3
import json

path = r"C:\\Users\\zidel\\Documents\\GitHub\\dJams\\database\\djams.db"
try:
    conn = sqlite3.connect(path)
except Error as e:
        print(e)
cursor = conn.cursor()
username=""
types=""
sunnylisten=""
sunnymood=""
rainylisten=""
rainymood=""
cloudylisten=""
cloudymood=""
workout=""
working=""
relaxing=""
#C:\Users\zidel\Documents\GitHub\dJams\templates
print("C:\\Users\\zidel\\Documents\\GitHub\\dJams\\templates\\example.json")
with open(r'C:\\Users\\zidel\\Documents\\GitHub\\dJams\\templates\\example.json') as survey:
    surveyAnswers = json.loads(survey.read())
    print(surveyAnswers)

for info in surveyAnswers:
    userID=surveyAnswers['Username']
    types=surveyAnswers['types']
    sunnylisten=surveyAnswers['sunnylisten']
    sunnymood=surveyAnswers['sunnymood']
    rainylisten=surveyAnswers['rainylisten']
    rainymood=surveyAnswers['rainymood']
    cloudylisten=surveyAnswers['cloudylisten']
    cloudymood=surveyAnswers['cloudymood']
    workout=surveyAnswers['workout']
    working=surveyAnswers['working']
    relaxing=surveyAnswers['relaxing']
    email = surveyAnswers['email']

cursor.execute("INSERT INTO Survey (UserID, types, sunnylisten, sunnymood, rainylisten, rainymood, cloudylisten, cloudymood, workout, relaxing,working) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
(userID, types, sunnylisten, sunnymood, rainylisten, rainymood, cloudylisten, cloudymood, workout, relaxing, working))
conn.commit()

cursor.close()
conn.close()
# sql_command = "INSERT INTO Survey (UserID, types, sunnylisten, sunnymood, rainylisten, rainymood, cloudylisten, cloudymood, workout, working, relaxing) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?,?,?);"
#
# cursor.execute(sql_command,(username, types, sunnylisten, sunnymood, rainylisten, rainymood, cloudylisten, cloudymood, workout, working, relaxing))
