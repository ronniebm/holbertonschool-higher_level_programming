/* a Javascript script that fetches from
https://fourtonfish.com/hellosalut/?lang=fr
and displays the value of hello from that
fetch in the HTML’s tag DIV#hello. */

const $ = window.$;

$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (resp) {
  $('#hello').text(resp.hello);
});
