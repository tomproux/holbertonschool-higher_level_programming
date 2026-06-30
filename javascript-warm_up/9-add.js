#!/usr/bin/node

function add(a, b) {
  return a + b;
}

const nb1 = Number(process.argv[2]);
const nb2 = Number(process.argv[3]);

console.log(add(nb1, nb2));
