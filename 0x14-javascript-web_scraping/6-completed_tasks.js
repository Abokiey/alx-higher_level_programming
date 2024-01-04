#!/usr/bin/node

// compute the nu,ber of tasks complete by user id

const request = require('request');
// const url = 'https://jsonplaceholder.typicode.com/todos'

function callback (error, _, body) {
  if (!error) {
    const todo = JSON.parse(body);
    const completed = {};
    todo.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
}

request(process.argv[2], callback);
