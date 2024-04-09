#!/usr/bin/node
const { argv } = require('process');
if (argv.length < 3) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Arguments found');
} else if (argv.lenght > 3){
  console.log('Arguments found');
}
