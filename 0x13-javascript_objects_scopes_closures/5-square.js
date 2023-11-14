#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square(Rectangle) {
  constructor (size) {
    super(size, size);
  }
}


module.exports = Square;
