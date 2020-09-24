/* a Javascript script that toggles the class
 of the HTML tag HEADER to red (#FF0000) when
 the user clicks on the tag DIV#toggle_header */

const $ = window.$;

$('div#toggle_header').click(function () {
  $('HEADER').toggleClass('green red');
});
