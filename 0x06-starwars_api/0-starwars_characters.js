#!/usr/bin/node

const request = require('request');

/**
 *
 * @param {number} id
 */
async function getStarWarsFilmCharacters(id) {
  await request.get(
    `https://swapi-api.alx-tools.com/api/films/${id}/`,
    (_, res, body) => {
      if (res.statusCode === 200) {
        const result = JSON.parse(body);
        for (const actor of result.characters) {
          actorNAme(actor);
        }
      }
    }
  );
}
/**
 * ### Get the actor name from the result gotten by the request
 * @param {string} url of the infomation
 */
async function actorNAme(url) {
  await request.get(url, (_, res, body) => {
    if (res.statusCode === 200) {
      console.log(JSON.parse(body).name);
    }
  });
}

const args = process.argv;
if (args.length < 3) {
  console.log('Usage: ./0-starwars_characters.js film_number');
  process.exit();
}

const filmId = parseInt(args[2]);
getStarWarsFilmCharacters(filmId);
