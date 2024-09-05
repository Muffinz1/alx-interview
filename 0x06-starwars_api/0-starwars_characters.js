#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movie_id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id;

request(url, function (err, res, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error('Error: Failed to retrieve movie');
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  printCharacters(characters, 0);
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], function (err, res, body) {
    if (err) {
      console.error('Error:', err);
      return;
    }

    if (res.statusCode !== 200) {
      console.error('Error: Failed to retrieve character');
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);

    printCharacters(characters, index + 1);
  });
}