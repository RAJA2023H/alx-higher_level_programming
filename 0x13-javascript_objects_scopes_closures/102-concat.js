#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const fileA = fs.readFileSync(process.argv[2], 'utf8');
const fileB = fs.readFileSync(process.argv[3], 'utf8');
const content = fileA + fileB;
fs.writeFileSync(process.argv[4], content, 'utf8');
