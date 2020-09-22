#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200 && resp.headers['content-type'] === 'application/json') {
    console.log(JSON.parse(body).title);
  }
});
