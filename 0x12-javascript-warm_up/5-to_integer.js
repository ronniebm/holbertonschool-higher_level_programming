#!/usr/bin/node
if (process.argv.slice(2).length == 0) {
  console.log('Not a number');
} else if (process.argv.slice(2).length == 1) {
    if (isNaN(parseInt(process.argv.slice(2)[0]))) {
      console.log('Not a number');
}   else {
      console.log(parseInt(process.argv.slice(2)[0]));
}

}
