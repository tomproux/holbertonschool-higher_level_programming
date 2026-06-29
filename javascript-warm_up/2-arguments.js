#!/usr/bin/node

const { args } = require('node:process');

if (args === 0)
{
    console.log('No argument');
}

else if (args === 1) 
{
    console.log('Argument found');
}

else if (args > 1) 
{
    console.log('Arguments found');
}