#!/usr/bin/node
const mylist = require('./100-data').list;
const map1 = mylist.map((x, index) => x * index);
console.log(mylist);
console.log(map1);
