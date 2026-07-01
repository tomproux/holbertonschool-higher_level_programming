#!/usr/bin/node
/* Write a JavaScript script that toggles the class
 of the `header` element when the user clicks
 on the tag id `toggle_header`
*/

const headColor = document.querySelector('header');

const setColor = document.querySelector('#toggle_header');
setColor.addEventListener('click', () => {
  if (headColor.classList.length === 0) {
    headColor.classList.add('green');
  } else if (headColor.classList.value.includes('green')) {
    headColor.classList.replace('green', 'red');
  } else if (headColor.classList.value.includes('red')) {
    headColor.classList.replace('red', 'green');
  }
});
