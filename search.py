import argparse

parser = argparse.ArgumentParser(description="Find text in some text")
parser.add_argument('inputText1', type=str, help="A string to look for")
parser.add_argument('inputText2', type=str, help="A string to compare")

args = parser.parse_args()
inputString1 = args.inputText1
inputString2 = args.inputText2

def search(a, b):
    if a in b:
        return b
    else:
        return False

outputString = search(inputString1, inputString2)
print(outputString)