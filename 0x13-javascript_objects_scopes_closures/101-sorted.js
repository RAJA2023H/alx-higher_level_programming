#!/usr/bin/node
const dict = require('./101-data').dict;
const Newdict = {};
for (const key in dict) {
  if (Newdict[dict[key]] === undefined) {
    Newdict[dict[key]] = [];
  }
  Newdict[dict[key]].push(key);
}
console.log(Newdict);
