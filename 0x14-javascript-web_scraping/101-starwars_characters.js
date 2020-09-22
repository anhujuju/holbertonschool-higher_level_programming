#!/usr/bin/node

const request = require('request');

request('https://swapi.co/api/films/' + process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200 && resp.headers['content-type'] === 'application/json') {
    let chars = JSON.parse(body).characters;
    let promiseArray = [];
    for (let i = 0; i < chars.length; i++) {
      promiseArray.push(new Promise((resolve, reject) =>
        request(chars[i], function (error, response, body) {
          if (error) {
            console.log(error);
          }
          if (err) {
            reject(err);
          } else if (response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          }
        })));
    }
    Promise.all(promiseArray).then((results) => {
      for (let i = 0; i < results.length; i++) {
        console.log(results[i]);
      }
    }).catch(err => console.log(err));
  }
});
