#!/usr/bin/node
//convert to a number.
const args = process.argv[2];

if(isNaN(args))
{
  console.log('Not a number');

}
else
{
  console.log(`My number: ${parseInt(arg)}`);
}
