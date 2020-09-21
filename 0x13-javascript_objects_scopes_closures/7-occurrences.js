#!/usr/bin/node

/**
 * A function that returns the number of
 * occurrences in a list.
 * -------------------------------------
 */

exports.nbOccurences = function (list, searchElement) {
  let ocurrence = 0;
  let item;

  for (item of list) {
    if (item === searchElement) {
      ocurrence++;
    }
  }

  return ocurrence;
};
