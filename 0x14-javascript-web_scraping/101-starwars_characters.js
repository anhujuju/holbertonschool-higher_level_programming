#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

function getCharacterRecursion (characters, low, high) {
  if (low < high) {
    const url = characters[low];
    request.get(url, (err, response, body) => {
      if (err) {
        console.log(err);
      } else if (response.statusCode === 200) {
        console.log(JSON.parse(body).name);
      }
      low += 1;
      getCharacterRecursion(characters, low, high);
    });
  }
}

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const n = characters.length;
    getCharacterRecursion(characters, 0, n);
  }
});