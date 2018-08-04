import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
files = [f for f in os.listdir(os.path.dirname(__file__)) if os.path.isfile(f)]
for f in files:
    print("files")
