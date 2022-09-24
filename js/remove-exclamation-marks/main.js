// INSTRUCTIONS
//Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

// SOLUTION

// function removeExclamationMarks(s) {
//   return s.replace("!", "");
// }

function removeExclamationMarks(s) {
  return s.replace(/!/g, '');
}

// RESOURCES
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace

// https://www.designcise.com/web/tutorial/how-to-fix-replaceall-is-not-a-function-javascript-error
