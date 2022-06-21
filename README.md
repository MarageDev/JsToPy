<h1 align="center"> JsToPy </h2>
<p align="center">
    <a href="https://discord.gg/8T2Ba2V2hj">
        <img src="https://img.shields.io/badge/DISCORD-Link-5662f6.svg?style=for-the-badge&logo=discord" alt="Discord Link">
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/GITHUB-Marage Dev-blue?style=for-the-badge&logo=github" alt="Github Profile">
    </a>
</p>
<h3 align="center">A simple method to create events from a JavaScript file and receive them in the Python file</h3>
<h6 align="center">  Normally there's no need to modify but if you've found a way to improve it or a fix to an error, let me know </h6>



## What is it ?
This is a simple method to create events from a JavaScript file, receive them in the Python file and then retrieve them in the JavaScript file
### How to download the files
To download the files you can clone the repository or download the .zip folder.
### How to run the program
  To run the program, open a terminal and type. Change `index.js` by the name of your JavaScript file if you changed it.
 ```
 node index.js
 ```
### The Result
In the terminal, you will see different logs which are the functions I already added as a demonstration. If everything is working fine, you should see
```
Data received from python : Arguments associated with this event -> Magic Note This is the event named :  CreateNewCustomFile

Data received from python : lorem ipsum abracadabra Meeska Moska Mickey Mouse 21
```
 These are the 2 events from `index.js` with their corresponding functions in Python in `main.py`. The first one creates a new `.txt` file with a name based on the first of the arguments of the event, and 2 other ones for the content : 
- argument 1 -> "Magic Note" ( the name of the file to create )
- argument 2 -> "This is the event named : " ( first of the 2 strings composing the text file )
- argument 3 -> "CreateNewCustomFile" ( the last of the 2 strings composing the text file )

And the second one returns a log with the differents arguments from the event inside : 
- argument 1 -> "Meeska Moska Mickey Mouse"
- argument 2 -> "50" ( which is a value determining the maximal range of the random integer )

## Documentation
The part below will describe how to use the code

### JavaScript part
This is the part of the program in `index.js`, you can find the whole code in the file aswell as the comments

The function in the file `index.js` named `sendEvent` handle the events of the program.
> Normally there's no need to modify but if you've found a way to improve it or a fix to an error, let me know
```js
function sendEvent (name, args){
    // Define the array and add the default values
    spawnerArgs = ['./main.py', `${name}`]

    // Check if the event contains arguments
    if(typeof args  !== 'undefined' ){
        // Add every arguments to the array "spawnerArgs"
        args.forEach(element => {
            spawnerArgs.push(element)
        });
    }else{
        // If it doesn't contain any arguments, do nothing
        console.log("Doesn't possess args")
    }

    // Add the event and its arguments from "spawnerArgs" and the receive part
    python_process = spawner('python', spawnerArgs)
    python_process.stdout.on('data', (data) => {
        console.log('Data received from python :', data.toString())
    })
}
```

Then, you can send events in from the JavaScript file using the method
> Don't forget to put the arguments inside of an array. You can add more than 2 arguments by adding a coma and entering the name of the next argument
```js
sendEvent('STRING - EVENT NAME', ['STRING - ARGUMENT 1','STRING - ARGUMENT 2'])
```

### Python part
This part is for the code in `main.py`

This is the most important part of the python file. The variable `event` receives the event from the JavaScript file and gets its second argument ( this is a part of `index.js` )
```js
['./main.py', 'STRING - EVENT NAME']
              ^^^^
```
Then, the array `args` will save the arguments of the event, it'll save only after the second element ( another reference to `index.js`, this part has been automatized )
```js
sendEvent('STRING - EVENT NAME',  ['STRING - ARGUMENT 1', 'STRING - ARGUMENT 2'])
                                  ^^^^                    ^^^^
python_process = spawner('python', './main.py', 'STRING - EVENT NAME',  [ 'STRING - ARGUMENT 1',  'STRING - ARGUMENT 2'])
                                                                          ^^^^                    ^^^^
```
```py
# Import sys
import sys

# Define the name of the event, it's the second argument
event = sys.argv[1]
# Define every arguments after the name of the event in an array
args = sys.argv[2:]
```

To add the python code of the events, you can create a function corresponding to the event and add it the number of arguments you registered previously in `index.js`
```js
sendEvent('CreateNewCustomFile', ['Magic Note','This is the event named : ','CreateNewCustomFile'])
```
and add in the Python code in `main.py`
```py
def CreateFile(fileName, stSentece, ndSentence):
    with open(f'{fileName}.txt', 'w') as f:
        f.write(f'{stSentece} {ndSentence}')
    return print(f'Arguments associated with this event -> {args[0]} {args[1]} {args[2]}') 
```
Then this function will be triggered by this part in `main.py`, you can add the arguments of the event here
```py
if event == 'CreateNewCustomFile':
    output = CreateFile(args[0],args[1],args[2])
```

## Credits
Marage

### License
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License][cc-by-nc-sa].
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
