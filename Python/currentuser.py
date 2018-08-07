import sys
currentuser=sys.argv[1]

text_file = open("currentuser.txt", "w")

text_file.write("Current User: " + currentuser)

text_file.close()
