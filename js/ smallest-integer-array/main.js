// INSTRUCTIONS
//Given an array of integers your solution should find the smallest integer.

// For example:

// Given [34, 15, 88, 2] your solution will return 2
// Given [34, -345, -1, 100] your solution will return -345
// You can assume, for the purpose of this kata, that the supplied array will not be empty.

// SOLUTION

class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min(...args)
  }
}

// RESOURCES
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/min

https://dev.to/sagar/three-dots---in-javascript-26ci

https://codeburst.io/what-are-three-dots-in-javascript-6f09476b03e1