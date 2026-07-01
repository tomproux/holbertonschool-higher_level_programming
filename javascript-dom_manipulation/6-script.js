#!/usr/bin/node
/* Write a JavaScript script that fetches the character `name`
    from URL
*/

const ActorName = document.querySelector('#character');

fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => { ActorName.textContent = data.name; });
  