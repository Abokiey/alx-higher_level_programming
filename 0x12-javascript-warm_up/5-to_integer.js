#!/usr/bin/node

const args = process.argv[2];

if (isNaN(args))
{
  console.log('Not a number');
}

if (!isNaN(args))
{
  console.log(`My number: ${parseInt(arg)}`);
}
