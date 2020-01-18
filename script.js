function getNewColor() {
	var symbols, color;
	
	symbols = "0123456789ABCDEF"
	
	color = "#"
	
	for(var i = 0; i < 6; i++) {
		color = color + symbols[Math.floor(Math.random() * 16)];
	}
	 document.getElementById("jumbotron").style.background = color;
	
}

$(document).ready(function() {

  var quote;
  var author;

  function getNewQuote() {
    $.ajax({
      url: 'http://api.forismatic.com/api/1.0/',
      jsonp: 'jsonp',
      dataType: 'jsonp',
      data: {
        method: 'getQuote',
        lang: 'en',
        format: 'jsonp'
      },
      success: function(response){
        author = response.quoteAuthor;
        if (author) {
		  quote = ('\"' +  response.quoteText + '\"' + " ");
		  $('#instructions').text('');
		  $('#quote').text(quote );
          $('#author').text('- ' + author);
          author = ('- ' + author)
        } else {
          /*$('#author').text('--unknown');
		  $('#quote')
          author = ('--unknown');*/
        }
      }
    });
    $('#tweetQuoteButton').prop('disabled', false);
  }

  $('#getQuoteButton').on('click', function(event) {
    event.preventDefault();
    getNewQuote();
	getNewColor();
  });

  $('#tweetQuoteButton').on('click', function(event) {
    event.preventDefault();
    window.open('https://twitter.com/intent/tweet/?text=' + encodeURIComponent(quote + author));
  });

});


