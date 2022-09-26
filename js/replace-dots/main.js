/* INSTRUCTIONS
The code provided is supposed replace all the dots . in the specified String str with dashes -

But it's not working properly.

Task
Fix the bug so we can all go home early.

Notes
String str will never be null.
*/

// SOLUTION
const replaceDots = (str) => str.split(".").join("-");

/*const replaceDots = function(str) {
  return str.replace(/[.]/g, '-');
}*/

/* RESOURCES
https://medium.com/problem-solving-using-codewars/codewars-fixme-replace-all-dots-83e568c70e40


var replaceDots = function(str) {
  // added the \ to escape special characters
  // added the g so that replace is run for all occurences in the string
    return str.replace(/\./g, '-');
  }
  */
