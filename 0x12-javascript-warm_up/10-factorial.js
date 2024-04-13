#!/usr/bin/node

function factorial (a) {
  if (a <= 1) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
const n1 = parseInt(process.argv[2]);
if (isNaN(n1)) {
  console.log(1);
} else {
  console.log(factorial(n1));
}
