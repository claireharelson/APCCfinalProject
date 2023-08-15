// Javascript to add autocomplete feature to html search form

$( function(){
	var options = [
		"1a62", "1a63", "1a6x", "1b12", "1bdx", "1bxd", "1bxw", "1c4t", "1e94", "1gmx", "1gn0", "1gs5", "1gsj", "1h3m", "1hqy", "1ht1", "1ht2", "1oh9", "1oha", "1ohb", "1ojg", "1qj3", "1qj5", "1qjo", "1qjp", "1xem", "1xen", "1xeo", "2bdo", "2bon", "2cgj", "2cgk", "2cgl", "2gj8", "2gj9", "2gja", "2i6w", "2ix1", "2kbc", "2m6r", "2m6s", "2mtq", "2opx", "2otc", "2uyt", "2uzz", "2v42", "2v43", "2vb2", "2vyc"
	];
	$( "#search" ).autocomplete({
		source: options,
		minLength: 1
	});
});

