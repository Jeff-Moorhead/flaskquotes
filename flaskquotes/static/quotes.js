var quote;
var movie;
var year;
var rank = Math.floor(Math.random() * 100);

function getNewQuote() {
    fade()
    quote = quotes.rank.Quote;
    movie = quotes.rank.Movie;
    year = quotes.rank.Year;
    var twitterLink = "https://twitter.com/intent/tweet?text=\"" +
    quote + "\"%20%20%20&hashtags=" + movie + ",freeCodeCamp" +
    ",FrontEndWebDev"
    $("#tweet-link").attr("href", twitterLink);
    var newIndex = Math.floor(Math.random() * 100);
    if (newIndex != rank) {
        rank = newIndex;
    }
    else {
        newIndex = Math.floor(Math.randon() * 100);
    }
}

function fade() {
    formatted = "#" + rank + " -  " + quote + " - from " + movie + " (year)";
    $(".quote").fadeOut(1000, function () {
        $(".quote").html("\"" + formatted + "\"");
        $(this).fadeIn(1000);
    });

    /*$(".movie").fadeOut(1000, function () {
        $(".movie").html("- " + movie);
        $(this).fadeIn(1000);
    });*/

    $(".btn-basic").fadeOut(1000, function () {
        $(this).fadeIn(1000);
    })
};
