#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movie_id = process.argv[2];
const a_url = 'https://swapi-api.hbtn.io/api/films/' + movie_id;

request(a_url, function (err, res, body) {
  if (err) {
    console.log('Error:', err);
    return;
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  getCharacters(characters, 0);
});

function getCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], function (err, res, body) {
    if (err) {
      console.log('Error:', err);
      return;
    }
    const character = JSON.parse(body);
    console.log(character.name);
    getCharacters(characters, index + 1);
  });
}


