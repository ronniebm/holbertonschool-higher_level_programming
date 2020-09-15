#!/usr/bin/node
if (Object.keys(process.argv.slice(2)).length == 0) {
  console.log('No argument');
} else if (Object.keys(process.argv.slice(2)).length == 1) {
  console.log('Argument found');
} else if (Object.keys(process.argv.slice(2)).length == 2) {
  console.log('Arguments found');
}
