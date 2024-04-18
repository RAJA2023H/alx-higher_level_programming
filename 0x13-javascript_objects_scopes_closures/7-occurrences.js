#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let N = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      N += 1;
    }
  }
  return N;
};
