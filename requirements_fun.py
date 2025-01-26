# Importing Base Packages
import os
import subprocess
import sys


# Defining a function to install required packages
def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Error installing dependencies. Check requirements.txt.")