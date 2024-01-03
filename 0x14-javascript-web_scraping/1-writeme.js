#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];

function error (err) {
  if (err) {
    console.log(err);
  }
}

fs.writeFile(path, content, 'utf-8', error);
