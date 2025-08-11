//process of taking output from one function and passing it to other in same line

let array = [
    {name: 'A', age: 14, gender: "M"},
    {name: 'B', age: 15, gender: "M"},
    {name: 'C', age: 16, gender: "F"},
    {name: 'D', age: 17, gender: "M"},
    {name: 'E', age: 18, gender: "M"},
    {name: 'F', age: 19, gender: "F"}
]

//Age of all men

let males = array.filter((obj)=>{
    return obj.gender == 'M';
})
console.log(males)

let ages = males.map((obj)=>{
    return obj.age;
})
console.log(ages)

//chaining will take output of males directly

let malesAges = array.filter((obj)=>{
    return obj.gender == 'M';
}).map((obj)=>{
    return obj.age;
})
console.log(malesAges)


//take sum of positives

const transactions = [1000, 3000, 4000, 2000, -898, 3800, -4500];

let positiveSum = transactions.filter((n)=>{
    return n>0;
}).reduce((acc, n)=>{
    let Sum = acc+n;
    return Sum;
}, 0)
console.log(positiveSum)