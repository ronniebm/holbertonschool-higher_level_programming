#!/usr/bin/node

// inherits from Square of 5-square.js
const Square5 = require('./5-square');

/**
 * A class Square that defines a square and
 * inherits from Square of 5-square.js
 * -------------------------------------------
 * size: Size of the square.
 */

class Square extends Square5 {
  charPrint (c) {
    if (typeof c !== 'undefined') {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      super.print();
    }
  }
}

const SquareObj = Square;
module.exports = SquareObj;
