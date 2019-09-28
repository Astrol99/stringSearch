import argparse

parser = argparse.ArgumentParser(description="Find text in some text")
parser.add_argument('inputText', type=str, help="A string to look for")

args = parser.parse_args()
inputString = args.inputText
outputString = ""

def search(a, b):
    pass