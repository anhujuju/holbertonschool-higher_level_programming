#!/usr/bin/node

const request = require('request');

request('https://swapi.co/api/films/' + process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200 && resp.headers['content-type'] === 'application/json') {
    let chars = JSON.parse(body).characters;
    for (let i = 0; i < chars.length; i++) {
      request(chars[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
