#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (const j in list) {
    if (list[j] === searchElement) {
      num++;
    }
  }
  return num;
};
