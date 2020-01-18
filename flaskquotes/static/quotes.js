function formatMovieData() {
    let moviedata = getRandomQuote()
    let twitterLink = getTwitterLink(moviedata)

    $("#tweet-link").attr("href", twitterLink);
    $(".quote").fadeOut(1000, function () {
        $(".quote").html("#" + moviedata.rank + " - " + moviedata.quote);
        $(this).fadeIn(1000);
    });

    $(".movie").fadeOut(1000, function () {
        $(".movie").html("- " + moviedata.movie + " (" + moviedata.year + ")");
        $(this).fadeIn(1000);
    });

    $(".btn-basic").fadeOut(1000, function () {
        $(this).fadeIn(1000);
    })

    $("#tweet-quote").attr("disabled", false);
}

function getRandomQuote() {
    let quote;
    let movie;
    let year;
    let rank = getRandomRank(); 

    console.log(rank);
    console.log(quotes[rank]);
    quote = quotes[rank].Quote;
    movie = quotes[rank].Movie;
    year = quotes[rank].Year
    console.log(quote);
    linkQuote = quote.split(" ").join("+");
    linkMovie = movie.split(" ").join("");

    return {"rank": rank, "quote": quote, "movie": movie, "year": year};
}

function getTwitterLink(moviedata) {
    quote = moviedata.quote;
    movie = moviedata.movie;
    
    linkQuote = quote.split(" ").join("+");
    linkMovie = movie.split(" ").join("+");

    return "https://twitter.com/intent/tweet?text=" +
    linkQuote + "%20%20%20&hashtags=" + linkMovie + ",Python" +
    ",Flask";
}

function getRandomRank() {
	return Math.floor(Math.random() * 100) + 1;
}
