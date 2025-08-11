//promises can be in pending, fulfilled or rejected state then settled
//takes callbacks resolve and reject
//catch and then

let myPromise = new Promise(function(resolve, reject){
    const a = "yey";
    const b = "nay";

    setTimeout(()=>{
        if(a == b){
            resolve("resolved")
        }else{
            reject("rejected")
        }
    }, 2000)

    // function chita(){
    //     if(a!=b){
    //         resolve("resolved")
    //     }else{
    //         reject("rejected")
    //     }
    // }
});

console.log(myPromise); //pending

myPromise.then((result)=>{
    console.log(result)
})

myPromise.catch((result)=>{
    console.log(result)
})