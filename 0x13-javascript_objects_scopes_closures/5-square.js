#!/usr/bin/node

// inherits from Rectangle of 4-rectangle.js
const Rectangle = require('./4-rectangle');

/**
 * A class Square that defines a square:
 * -------------------------------------------
 * size: Size of the square.
 */

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
