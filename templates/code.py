import os
import sys
import subprocess

hello = subprocess.check_output([sys.executable, "hello.py"])
print(hello)
