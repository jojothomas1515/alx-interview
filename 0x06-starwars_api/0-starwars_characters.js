#!/usr/bin/node

const request = require('request');

/**
 *
 * @param {number} id
 */
function getStarWarsFilmCharacters (id) {
  request.get(
    `https://swapi-api.alx-tools.com/api/films/${id}/`,
    (_, res, body) => {
      if (res.statusCode === 200) {
        const result = JSON.parse(body);
        const cName = result.characters.map((url) =>
          new Promise((resolve, reject) => {
            request.get(url, (err, res, body) => {
              if (err) {
                reject(err);
              }
              resolve(JSON.parse(body).name);
            });
          })
        );
        Promise.all(cName)
          .then(res => console.log(res));
      }
    }
  );
}

const args = process.argv;
if (args.length < 3) {
  console.log('Usage: ./0-starwars_characters.js film_number');
  process.exit();
}

const filmId = parseInt(args[2]);
getStarWarsFilmCharacters(filmId);
