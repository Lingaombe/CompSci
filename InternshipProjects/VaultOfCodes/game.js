const car = document.getElementById("carr");
let x, y;

window.addEventListener('keydown', function(x){
    if(x.key == "w" || x.key == "W"){
        alert("w");
    }
    else if(x.key == "a" || x.key == "A"){
        alert("a");
    }
    else if(x.key == "d" || x.key == "D"){
        alert("d");
    }
    else if(x.key == "s" || x.key == "S"){
        alert("s");
    }
})