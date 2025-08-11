//map returns a new array based on passed array

const transactions = [1000, 3000, 4000, 2000, -898, 3800, -4500];
const inrtoDollar = 80;

const Dollar = transactions.map(function(i){
    return (i/inrtoDollar).toFixed(0); //no decimals
})

console.log(Dollar)

//forEach loops through array but doesnt return array

const Dollar1 = transactions.forEach(function(i){
    console.log(i/inrtoDollar);
})

console.log(Dollar1); // This will log undefined

//find returns first instance to satisfy condition

const negative = transactions.find((n)=>{
    return n<0;
})
console.log(negative)

//findIndex returns first instance index
const negativeIndex = transactions.findIndex((n)=>{
    return n<0;
})
console.log(negativeIndex)

//some returns boolean based on condition ie when atleaset one element in array satisfies condition

const checkPositive = transactions.some((n)=>{
    return n>0
})
console.log(checkPositive)

//every needs all elements to satisfy

const checkAll = transactions.every((n)=>{
    return n>0
})
console.log(checkAll)

//filter returns array with elements that satisfy

const filter = transactions.filter((n)=>{
    return n%2==0;
})
console.log(filter)

//reduce returns single result ie sum of array elements, takes 4 args

// total. Required. The initialValue, or the previously returned value of the function.
// currentValue. Required. The value of the current element.
// currentIndex. Optional. The index of the current element.
// arr. Optional. The array the current element belongs to.

const sum = transactions.reduce((acc, value)=>{
    let Sum = acc+value; //value being element
    return Sum
} , 0 /* acumulator will be keeping result*/ )

console.log(sum)

const Multi = transactions.reduce((acc, value)=>{
    let multi = acc*value; //value being element
    return multi
} , 1 /* acumulator will be keeping result*/ )

console.log(Multi)