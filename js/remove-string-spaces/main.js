// INSTRUCTIONS
//Simple, remove the spaces from the string, then return the resultant string.

// SOLUTION
function noSpace(x) {
  return x.replace(/\s+/g, "");
}

// function noSpace(x) {
//   return x.split(" ").join("");
// }

// function noSpace(x){
//   let arr =  x.split(' ');
//   return arr.reduce((a,b)=>a+b);
//  }

// RESOURCES
// https://stackoverflow.com/questions/5963182/how-to-remove-spaces-from-a-string-using-javascript#5963202
