#!/usr/bin/node

/* read and print contents of a file */

const fs = require('fs');
const path = process.argv[2];

fs.readFile(path, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});