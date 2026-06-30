#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(Number);

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const num of numbers) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  console.log(secondLargest);
}
