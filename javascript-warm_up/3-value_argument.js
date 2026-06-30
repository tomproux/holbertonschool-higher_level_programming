#!/usr/bin/node

const [, , firstArg] = process.argv;

if (firstArg === undefined) {
    console.log('No argument');
} else {
    console.log(firstArg);
}
