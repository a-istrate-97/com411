import os
def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following files: ", end="")
    for file in os.listdir(path):
        print(file, end ="")

def run():
    print("Processing...")
    cwd()

run()