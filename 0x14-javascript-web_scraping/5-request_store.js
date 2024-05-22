#!/usr/bin/node
const fs = require('fs');
const request = require('request');
if (process.argv.length < 3) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}
const url = process.argv[2];
const path = process.argv[3];

request(url, (err, res, body) => {
  if (err) console.log(err);
  fs.writeFileSync(path, body, { encoding: 'utf8' });
});
