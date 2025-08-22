//setTimeout takes callback and time

function greet(){
    console.log("Bhobho!");
}

setTimeout(greet, 3000);

console.log("This will run first, before the greet function.");


//setInterval takes callback and timer and runs after each interval

function Moni(){
    console.log("Moni kwa inu!.");
}

timer = setInterval(Moni, 2000); //runs forever if no stopper ie clearInterval

//clearInterval takes function of setInterval
//setTimeout with clearTimeout

setTimeout(function(){
    clearInterval(timer);
}, 5000); //stop after 5 seconds