# Import sys
import sys

# Optional import, it is just present for the demonstration
import random

# Define the name of the event, it's the second argument
event = sys.argv[1]
# Define every arguments after the name of the event in an array
args = sys.argv[2:]

# Add the functions
def CreateFile(fileName, stSentece, ndSentence):
    with open(f'{fileName}.txt', 'w') as f:
        f.write(f'{stSentece} {ndSentence}')
    return print(f'Arguments associated with this event -> {args[0]} {args[1]} {args[2]}') 

def Lorem(additionalSentence, randomIntMax):
    return print(f'lorem ipsum abracadabra {additionalSentence} {random.randint(0,int(randomIntMax))}') 

# Receive the events sent from the javascript file and assign them an action
if event == 'CreateNewCustomFile':
    output = CreateFile(args[0],args[1],args[2])

if event == 'LoremIpsumTest':
    output =  Lorem(args[0],args[1])
