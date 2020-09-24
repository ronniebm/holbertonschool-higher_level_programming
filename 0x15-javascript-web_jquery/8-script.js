/* a Javascript script that fetches and lists all
movies title by using this URL:
https://swapi-api.hbtn.io/api/films/?format=json */

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (resp) {
  for (var i = 0; i < resp.results.length; i++) {
    $('#list_movies').append(`<li>${resp.results[i].title}</li>`);
  }
});
