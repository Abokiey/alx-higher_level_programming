#!/usr/bin/node

let x = parseInt(process.argv[2]);
if (Number.isNaN(x))
{
  console.log('Missing number of occurrences');
}
for (let i = 0; i < x; i++)
{
  console.log('C is fun');
}
