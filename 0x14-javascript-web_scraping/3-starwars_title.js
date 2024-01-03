#!/usr/bin/node

// print the starwars movie where the ep no. matches an int

const request = require('request');
const movieid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieid;

function callback (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
}

request.get(url, callback);
