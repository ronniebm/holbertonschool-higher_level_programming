#!/usr/bin/node

/* A script that writes a string to a file
 */

const fs = require('fs');
const argv = process.argv;
const filePath = argv[2];
const string = argv[3];

fs.writeFile(filePath, string, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
