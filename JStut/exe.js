let ar = [1,2,3]

let ar2 = ar.map(num=>num*2)
let ar1 = ar.filter(num=>num%2==0)
console.log(ar.shift())
console.log(ar.pop())
console.log(ar2)
console.log(ar1)
console.log(ar)
ar.push(10)
console.log(ar)