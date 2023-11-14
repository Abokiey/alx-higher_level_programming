#!/usr/bin/node

exports.esrever = function (list) {
  let count = list.length - 1;
  const newlist = [];
  while (count >= 0) {
    newlist.push(list[count]);

    count--;
  }
  return newlist;
};
