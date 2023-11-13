#!/usr/bin/node
/* search biggest number */
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
  process.exit(0);
}

for (let j = 0; j < args.length; j += 1) {
  args[j] = parseInt(args[j], 10);
}

args.sort((a, b) => a - b);
console.log(args[args.length - 2]);
