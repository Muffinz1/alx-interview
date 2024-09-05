#!/usr/bin/node

const request = require('request');

const fetchCharacter = (url, callback) => {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    try {
      const character = JSON.parse(body).name;
      console.log(character);
    } catch (err) {
      console.error('Error parsing JSON:', err);
    }
    callback();
  });
};

const fetchFilmCharacters = (filmId) => {
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

  request(filmUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    try {
      const characters = JSON.parse(body).characters;

      const fetchNextCharacter = (index) => {
        if (index < characters.length) {
          fetchCharacter(characters[index], () => fetchNextCharacter(index + 1));
        }
      };

      fetchNextCharacter(0);
    } catch (err) {
      console.error('Error parsing JSON:', err);
    }
  });
};

fetchFilmCharacters(process.argv[2]);
