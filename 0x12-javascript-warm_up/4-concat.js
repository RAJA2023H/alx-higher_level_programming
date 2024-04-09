#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args[2]) {
  console.log(args[2], 'is' , args[3] ? args[3] : 'undefined');
} else {
	console.log('undefined is undefined');
}

