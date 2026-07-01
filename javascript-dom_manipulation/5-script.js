#!/usr/bin/node
/* Write a JavaScript script that updates the text
    of the `header` element to `New Header!!!`
*/

const UpdateHeader = document.querySelector('header');

const setHeader = document.querySelector('#update_header');
setHeader.addEventListener('click', () => {
  UpdateHeader.textContent = 'New Header!!!';
});
