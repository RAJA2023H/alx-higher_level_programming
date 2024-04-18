#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(Rectangle.width, Rectangle.height);
    this.width = this.height = size;
  }
}
module.exports = Square;
