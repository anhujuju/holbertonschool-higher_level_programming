#!/usr/bin/node

const request = require('request');

const oauth =
  { consumer_key: process.argv[2],
    consumer_secret: process.argv[3]
  };

const url = 'https://api.twitter.com/1.1/search/tweets.json';

const qs = { q: process.argv[4], count: 20 };

request.get({ url: url, oauth: oauth, qs: qs, json: true }, function (e, r, body) {
  if (e) {
    console.log(e);
  } else if (r.statusCode === 200) {
    let statuses = body.statuses;
    for (let i = 0; i < 5 && i < statuses.length; i++) {
      let stat = statuses[i];
      let s = '[' + stat.id + '] ' + stat.text + ' by ' + stat.user.name;
      console.log(s);
    }
  }
});
