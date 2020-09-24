/* a Javascript script that adds the class
   red to the HTML tag HEADER to red (#FF0000)
   when the user clicks on the tag DIV#red_header */

const $ = window.$;

$('div#red_header').click(function () {
  $('HEADER').addClass('red');
});
