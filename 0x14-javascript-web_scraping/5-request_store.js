#!/usr/bin/node

// get the content of a file and store in a file

const request = require('request');
const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');

request(url).pipe(fs.createWriteStream(path));
