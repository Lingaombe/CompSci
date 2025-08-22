//Adaptive menu 

const showmenu = document.getElementById("open");
const hidemenu = document.getElementById("close");
const menu = document.getElementById("menu");
const mode = document.getElementById("mode");


showmenu.addEventListener('click', function() {
    menu.style.display = 'block';
})

hidemenu.addEventListener('click', function() {
    menu.style.display = 'none';
})

//Cart counter

const count = document.getElementById("count");
const coun = document.getElementById("coun");
let num = 0;

function add(){
    num++;
    count.textContent = num;
    coun.textContent = num;
}

//mode

let c = 0;

mode.onclick = function(){
    c++;
    if(c%2==1){
        document.body.style.background = 'black';
        document.body.style.color = 'white';
    }
    else{
        document.body.style.background = 'white';
        document.body.style.color = 'black';
    }
    console.log("hehe");
}

//scroll effect

const arrow1 = document.getElementById("arrow1");
const arrow2 = document.getElementById("arrow2");
const review = document.getElementById("scroll");

arrow1.addEventListener('click', function(){
    review.style.transform = 'translateX(-100vw)';
})
arrow2.addEventListener('click', function(){
    review.style.transform = 'translateX(100vw)';;
})