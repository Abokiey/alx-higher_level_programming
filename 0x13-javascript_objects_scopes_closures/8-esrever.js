#!/usr/bin/node

exports.esrever = function (list) {
  let count = list.length - 1;
  const new_list = [];
  while (count >= 0) {
    new_list.push(list[count]);

    count--;
  }
  return new_list;
};
