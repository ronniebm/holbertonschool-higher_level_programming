#!/usr/bin/node

/**
 * A class Rectangle that defines a rectangle:
 * -------------------------------------------
 * w: width of a Rectangle.
 * h: height of a Rectangle.
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log(('X'.repeat(this.width)));
    }
  }
}

module.exports = Rectangle;
