#!/usr/bin/node

/* A script that prints all characters
 * of a Star Wars movie:
 */

const request = require('request');
const args = process.argv.slice(2);
const url = 'http://swapi.co/api/films/' + args[0];

const options = {
  url: url,
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Accept-Charset': 'utf-8'
  }
};

request(options, (err, res, body) => {
  if (err) { throw err; }
  const myList = JSON.parse(body).characters;
  for (let i = 0; i < myList.length; i++) {
    request({ url: myList[i], method: 'GET' }, (err, res, body) => {
      if (err) { console.log('Error'); }
      console.log(JSON.parse(body).name);
    });
  }
});
