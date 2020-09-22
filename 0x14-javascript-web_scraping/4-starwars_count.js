#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200) {
    let results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      let chars = results[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].includes('/18')) {
          count++;
          j = chars.length;
        }
      }
    }
    console.log(count);
  }
});
