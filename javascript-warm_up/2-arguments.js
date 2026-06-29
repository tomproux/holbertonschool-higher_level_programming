#!/usr/bin/node

const args = process.argv.slice(3);

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
