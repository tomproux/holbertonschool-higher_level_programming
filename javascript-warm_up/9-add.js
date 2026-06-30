#!/usr/bin/node

function add (nb1, nb2) {
  return nb1 + nb2;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

console.log(add(a, b));
