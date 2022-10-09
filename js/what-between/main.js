// INSTRUCTIONS
//Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

// For example:

// a = 1
// b = 4
// --> [1, 2, 3, 4]

// SOLUTION
function between(a, b) {
  let list = [];
  for (let i = a; i <= b; i++) {
    list.push(i);
  }
  return list;
}

// RESOURCES: https://stackoverflow.com/questions/8069315/create-array-of-all-integers-between-two-numbers-inclusive-in-javascript-jquer
