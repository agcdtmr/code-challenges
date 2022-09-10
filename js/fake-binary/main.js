// INSTRUCTIONS

// Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

// Note: input will never be an empty string

// SOLUTION

function fakeBin(x) {
  //   const arr = Array.from(x)
  //   const parsed = arr.map( function(str) { return parseInt(str) })
  //   const converted = parsed.map(num => num >= 5 ? 1 : 0)
  //   return converted.join("")

  return Array.from(x)
    .map((str) => parseInt(str))
    .map((num) => (num >= 5 ? 1 : 0))
    .join("");
}

// RESOURCES
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseInt

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join
