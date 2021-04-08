/* 

A Pythagorean traplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

*/

let c

for (let a = 1; a < 999; a++) {
    for (let b = 2; b < 999; b++) {
        c = Math.sqrt(Math.pow(a,2) + Math.pow(b,2))
        if (Number.isInteger(c) && a < b && b < c && (a+b+c==1000)) {
            console.log(a*b*c)
            break
        }
    }
}
