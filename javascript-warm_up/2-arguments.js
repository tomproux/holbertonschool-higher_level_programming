#!/usr/bin/node

const args = process.argv.slice(3);

if (args.lenght === 0)
{
    console.log('No argument');
}

else if (args.lenght === 1) 
{
    console.log('Argument found');
}

else if (args.lenght > 1) 
{
    console.log('Arguments found');
}
