import sys
import random

# Define the name of the event, it's the second argument
event = sys.argv[1]
# Define every arguments after the name of the event in an array
args = sys.argv[2:]

# Add the functions
def printC(fileName, stSentece, ndSentence):
    with open(f'{fileName}.txt', 'w') as f:
        f.write(f'{stSentece} {ndSentence}')
    return print(f'Commands associated with this event -> {sys.argv[2]} {sys.argv[3]}') 
def lorem():
    return print(f'lorem ipsum abracadabra {random.randint(0,10)}') 

# Receive the events sent from the javascript file and assign them an action
if event == 'aaa':
    output = printC(args[0],args[1],args[2])

if event == 'kal':
    output =  lorem()
