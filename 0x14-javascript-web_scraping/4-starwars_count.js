#!/usr/bin/node
const request = require('request')
const url = process.argv[2]

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err)
  } else {
    if (response.statusCode === 200) {
      const rJson = JSON.parse(body)
      let count = 0
      for (const film of rJson.results) {
        for (const character of film.characters) {
          if (character.endsWith('/18/')) {
            count++
            break
          }
        }
      }
      console.log(count)
    }
  }
})
