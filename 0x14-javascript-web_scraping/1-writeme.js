#!/usr/bin/node
// script that reads and prints the content of a file.
const args = process.argv.slice(2);
const fs = require('fs');
const filepath = args[0];
const str = args[1];

if (args.length < 2) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}

fs.writeFile(filepath, str, 'utf8', (err) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
});
