#!/usr/bin/node
// prints first argument
const { argv } = require('process');
if (argv.length <= 2) console.log('No argument');
if (argv.length === 3) console.log('Arguments found');
if (argv.lenght > 3) console.log('Arguments found');
