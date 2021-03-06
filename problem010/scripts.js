/* 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

*/

const esPrimo = (n) => {
    for (let i = 2; i <= (Math.round(Math.sqrt(n))); i++) {
        if (n%i===0) return false
    }
    return true
}

let sum = 0

for (let i = 2; i < 2000000; i++) {
    if (esPrimo(i)) sum += i
}

console.log(sum)
