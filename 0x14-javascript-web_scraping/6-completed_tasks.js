#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.log(err);
  const result = {};
  const data = JSON.parse(body);
  for (const task of data) {
    if (task.completed) {
      result[task.userId] = (result[task.userId] || 0) + 1;
    }
  }
  console.log(result);
});
