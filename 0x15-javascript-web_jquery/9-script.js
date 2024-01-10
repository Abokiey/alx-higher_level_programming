const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'

$('document').ready(() => {
$.get(url, (data) => {
	$('DIV#hello').text(data.hello);
	})
});
