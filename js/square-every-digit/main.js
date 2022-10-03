// INSTRUCTIONS
//Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

// For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

// Note: The function accepts an integer and returns an integer

// SOLUTION
function squareDigits(num) {
  const numAsStr = num.toString();
  const arr = numAsStr.split("");
  const arrayStr = arr
    .map((val) => {
      const convertedNum = parseInt(val);

      return convertedNum * convertedNum;
    })
    .join("");
  return parseInt(arrayStr);
}

// RESOURCES
