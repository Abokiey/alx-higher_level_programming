#!/usr/bin/node
/* print the first argument */

const args = process.argv.slice(2);
console.log(args[0] ? args[0] : 'No argument');
