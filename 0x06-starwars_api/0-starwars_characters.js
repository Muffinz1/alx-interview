#!/usr/bin/node

const request = require('request-promise-native');

const fetchCharacter = async (url) => {
  try {
    const response = await request(url);
    const character = JSON.parse(response).name;
    console.log(character);
  } catch (error) {
    console.error(error);
  }
};

const fetchFilmCharacters = async (filmId) => {
  try {
    const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
    const response = await request(apiUrl);
    const characters = JSON.parse(response).characters;

    for (const url of characters) {
      await fetchCharacter(url);
    }
  } catch (error) {
    console.error(error);
  }
};

fetchFilmCharacters(process.argv[2]);
