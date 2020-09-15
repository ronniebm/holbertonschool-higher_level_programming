#!/usr/bin/node
if (process.argv.slice(2).length === 0) {
  console.log('Missing number of occurrences');
} else if (process.argv.slice(2).length === 1) {
  if (isNaN(parseInt(process.argv.slice(2)[0])) === false) {
    let i;
    for (i = 0; i < parseInt(process.argv.slice(2)[0]); i++) {
      console.log('C is fun');
    }
  }
}
