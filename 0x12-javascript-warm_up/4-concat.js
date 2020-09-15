#!/usr/bin/node
if (process.argv.slice(2).length === 0) {
  console.log('undefined is undefined');
} else if (process.argv.slice(2).length === 1) {
  console.log(process.argv.slice(2)[0] + ' is undefined');
} else if (process.argv.slice(2).length === 2) {
  console.log(process.argv.slice(2)[0] + ' is ' + process.argv.slice(2)[1]);
}
