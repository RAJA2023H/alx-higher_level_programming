#!/usr/bin/node
// display the status code of a GET request.

const https = require('https');
const url = process.argv[2];
if (process.argv.length < 3) {
  console.error('Usage: node script.js <url>');
  process.exit(1);
}

https.get(url, (res) => {
  console.log('Code:', res.statusCode);
}).on('error', (err) => {
  console.error('Error:', err.message);
});
