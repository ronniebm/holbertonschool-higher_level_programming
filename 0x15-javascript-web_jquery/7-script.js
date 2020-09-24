/* a Javascript script that fetches and replaces
the name of this URL:
https://swapi-api.hbtn.io/api/people/5/?format=json */

const $ = window.$;

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (resp) {
  $('#character').text(resp.name);
});
