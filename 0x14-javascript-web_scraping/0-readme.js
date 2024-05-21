#!/usr/bin/node
// script that reads and prints the content of a file.
const args = process.argv.slice(2);
const fs = require('fs');
const filepath = args[0];

if (args.length < 1) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}

fs.readFile(filepath, 'utf8', (err, content) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  console.log(content);
});
