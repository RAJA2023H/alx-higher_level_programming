#!/usr/bin/node
// display the status code of a GET request.

const request = require('request');
const url = process.argv[2];
if (process.argv.length < 3) {
  console.error('Usage: node script.js <url>');
  process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.error('Error:', error.message);
  } else {
    console.log('Code:', response.statusCode);
  }
});
