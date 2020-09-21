#!/usr/bin/node

/**
 * A class Rectangle that defines a rectangle:
 * -------------------------------------------
 * w: width of a rectangle.
 * h: height of a rectangle.
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
