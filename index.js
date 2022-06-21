const spawner = require('child_process').spawn;
let python_process = spawner('python', ['./main.py'])

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

// Add events
sendEvent('CreateNewCustomFile', ['Magic Note','This is the event named : ','CreateNewCustomFile'])
sendEvent('LoremIpsumTest', ['Meeska Moska Mickey Mouse','50'])
