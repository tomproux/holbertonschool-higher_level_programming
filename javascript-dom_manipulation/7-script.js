#!/usr/bin/node
/* Write a JavaScript script that fetches and
    lists the `title` for all movies by using URL
*/

const FilmList = document.querySelector('#list_movies');

fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    for (let index = 0; index < data.results.length; index++) {
      const NewFilm = document.createElement('li');
      NewFilm.textContent = data.results[index].title;
      FilmList.appendChild(NewFilm);
    }
  });
