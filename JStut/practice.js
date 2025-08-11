const myPromise = new Promise((resolve, reject)=>{
    const a = 10
    const b = 10

    setTimeout( ()=>{
        if(a==b){
            resolve("resolved")
        }
        else{
            reject("rejected")
        }
    }, 2000)
})

myPromise.then((result)=>{
    console.log(result)
}).catch((err)=>{
    console.log(err)
})

console.log("hi, me first")